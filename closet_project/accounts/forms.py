from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password


class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    class Meta():
        model = Users
        fields = ('username', 'email', 'password')
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('パスワードが異なります')
        
    def save(self, commit=False):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        
        try:
            validate_password(password, user)
        except forms.ValidationError as error:
            self.add_error('password', error)
        
        user.set_password(password)
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.CharField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())
    
class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
        
    class Meta:
        model = Users
        fields = ('username', 'email')
        
class PasswordChangeForm(forms.Form):
    
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('パスワードが異なります')
        
    def save(self, user, commit=True):
        password = self.cleaned_data["password"]
        user.set_password(password)  # パスワードのハッシュ化
        if commit:
            user.save()
        return user