from django.shortcuts import render, redirect
from . import forms
from django.core.exceptions import ValidationError
from .models import UserActivateTokens
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from django.contrib.auth import password_validation

User = get_user_model()

def home(request):
    return render(
        request, 'accounts/home.html'
    )
    
def regist(request):
    regist_form = forms.RegistForm(request.POST or None)
    if regist_form.is_valid():
        try:
            user = regist_form.save(commit=False)
            user.is_active = True  # アカウントを有効にする
            user.save()
            return redirect('accounts:user_login')
        except ValidationError as e:
            regist_form.add_error('password', e) 
    return render(
        request, 'accounts/regist.html', context={
            'regist_form': regist_form,
        }
    )
    
def activate_user(request, token):
    user_activate_token = UserActivateTokens.objects.activate_user_by_token(token)
    if user_activate_token:
        return HttpResponse("ユーザーをアクティブ化しました。")
    else:
        return HttpResponse("トークンが無効です。")
    
    return render(request, 'accounts/activate_user.html')
    
def user_login(request):
    login_form = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                if user.is_staff:  
                    return redirect('admin:index')
                else:
                    return redirect('accounts:home')
            else:
                raise ValidationError('ユーザがアクティブではありません')
        else:
            messages.warning(request, 'メールかパスワードが間違っています')
    return render(
        request, 'accounts/user_login.html', context={
            'login_form': login_form,
        }
    )
    

    
@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:home')

@login_required
def user_edit(request):
    user_edit_form = forms.UserEditForm(request.POST or None, request.FILES or None, instance=request.user)
    if user_edit_form.is_valid():
        user_edit_form.save()
    return render(request, 'accounts/user_edit.html', context={
        'user_edit_form': user_edit_form,
    })
    
@login_required
def change_password(request):
    if request.method == 'POST':
        password_change_form = forms.PasswordChangeForm(data=request.POST)
        if password_change_form.is_valid():
            password = password_change_form.cleaned_data['password']
            confirm_password = password_change_form.cleaned_data['confirm_password']

            if password != confirm_password:
                messages.error(request, 'パスワードが一致しません。')
            else:
                user = request.user
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
                return redirect('accounts:home')
    else:
        password_change_form = forms.PasswordChangeForm()

    return render(
        request, 'accounts/change_password.html', context={
            'password_change_form': password_change_form
        }
    )
    

class CustomLoginView(LoginView):
    template_name = 'accounts/user_login.html'

    def get_success_url(self):
        user = self.request.user

        if user.is_staff:
            # 管理者ユーザーの場合は管理者サイトへ遷移
            return reverse('admin:index')
        elif user.is_active:
            # activeなユーザーの場合はHOME画面へ遷移
            return reverse('accounts:home')
        else:
            # 上記の条件に合致しない場合、デフォルトの遷移先になります
            return super().get_success_url()
