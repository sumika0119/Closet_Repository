from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from .models import Categories, Clothes, Colors, Clothe_Colors
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from PIL import Image
import os

# Create your views here.    

@login_required
def create_clothe(request):
    categories = Categories.objects.all() 
    colors = Colors.objects.all()
    if request.method =='POST':
        create_clothe_form = forms.CreateClotheForm(request.POST, request.FILES)
        if create_clothe_form.is_valid():
            title = create_clothe_form.cleaned_data['title']
            picture = create_clothe_form.cleaned_data['picture']
            price = create_clothe_form.cleaned_data['price']
            purchase_date = create_clothe_form.cleaned_data['purchase_date']
            store_name = create_clothe_form.cleaned_data['store']
            category_name = create_clothe_form.cleaned_data['category']
            selected_colors = create_clothe_form.cleaned_data['color']
            
            category_instance = Categories.objects.filter(category_name=category_name).first()
            color_instance_list = [] 
            for color_id in selected_colors:
                color_instance = color_id
                if color_instance:
                    color_instance_list.append(color_instance)
            
            new_clothe = create_clothe_form.save(commit=False)
            new_clothe.user = request.user
            
            if 'picture' in request.FILES:
                image = Image.open(request.FILES['picture'])
                desired_width = 300
                desired_height = 200
                resized_image = image.resize((desired_width, desired_height))
        

                new_clothe.picture = request.FILES['picture']
                           
            if category_instance:
                new_clothe.category = category_instance
                
            new_clothe.save()

            for color_instance in color_instance_list:
                Clothe_Colors.objects.create(clothe=new_clothe, color=color_instance)
            
            return redirect('boards:list_clothe')   
        
    
            
    else:
        create_clothe_form = forms.CreateClotheForm()
        
    return render(
        request, 'boards/create_clothe_form.html', context={
            'create_clothe_form': create_clothe_form,
            'categories': categories, 
            'colors': colors,
        }
    )

@login_required    
def list_clothe(request):
    sort_option = request.GET.get('sort', '')  # URL パラメーターからソートオプションを取得
    
    color = Colors.objects.all()
    category = Categories.objects.all()

    selected_color = request.GET.get('color')
    selected_category = request.GET.get('category')
    search_query = request.GET.get('search') 
    
    clothe = Clothes.objects.filter(user=request.user)
    
    if selected_color:
        clothe = clothe.filter(color__color_name=selected_color)

    if selected_category:
        clothe = clothe.filter(category__category_name=selected_category)
    
    if search_query:
        clothe = clothe.filter(
            Q(title__icontains=search_query) |
            Q(store__icontains=search_query) 
        )
                
    if sort_option == 'price_low':
        clothe = clothe.order_by('price')
    elif sort_option == 'price_high':
        clothe = clothe.order_by('-price')
    elif sort_option == 'date_new':
        clothe = clothe.order_by('-purchase_date')
    elif sort_option == 'date_old':
        clothe = clothe.order_by('purchase_date')
    
    return render(
        request, 'boards/list_clothe.html', context={
            'clothe': clothe,
            'color': color,
            'category': category,
            'selected_color': selected_color,
            'selected_category': selected_category,
            'search_query': search_query,
        }
    )

@login_required
def detail_clothe(request, pk):
    clothe = get_object_or_404(Clothes, pk=pk)
    print(f"Color: {clothe.color.all()}")  # デバッグ用のログ出力
    return render(
        request, 'boards/detail_clothe.html', context={
            'clothe': clothe,
        }
    )
    
@login_required
def edit_clothe(request, pk):
    categories = Categories.objects.all()
    colors = Colors.objects.all()
    
    clothe=get_object_or_404(Clothes, pk=pk)
    
    if clothe.user.pk != request.user.pk:
        raise Http404
    
    if request.method == 'POST':
        print('POST request received')
        edit_clothe_form = forms.CreateClotheForm(request.POST or None, request.FILES or None, instance=clothe)
        if edit_clothe_form.is_valid():
            edit_clothe_form.save()
            return redirect(
                'boards:detail_clothe', 
                pk=pk
            ) 
    else:
        edit_clothe_form = forms.CreateClotheForm(instance=clothe)
            
    return render(
        request, 'boards/edit_clothe.html', context={
            'edit_clothe_form':edit_clothe_form,
            'pk': pk,
            'categories': categories,
            'colors': colors,
        }
    )

@login_required
def delete_clothe(request, pk):
    deleted_clothe = get_object_or_404(Clothes, pk=pk)
    if request.method == 'POST':
        deleted_clothe.delete()  # 服を削除
        return redirect('boards:delete_clothe_complete')
    
    return render(
        request, 'boards/delete_clothe.html', context={
            'clothe': deleted_clothe
        }
    )

  
def delete_clothe_complete(request):
    return redirect('boards:list_clothe')  