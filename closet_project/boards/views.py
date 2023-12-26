from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from .models import Categories, Clothes

# Create your views here.
def create_clothe(request):
    if request.method == 'POST':
        create_clothe_form = forms.CreateClotheForm(request.POST or None)
        if create_clothe_form.is_valid():
            title = create_clothe_form.cleaned_data['title']
            picture = create_clothe_form.cleaned_data['picture']
            price = create_clothe_form.cleaned_data['price']
            purchase_data = create_clothe_form.cleaned_data['purchase_data']
            store_name = create_clothe_form.cleaned_data['store']
            category_name = create_clothe_form.cleaned_data['category']
            
            category_instance = Categories.objects.get(category_name=category_name)
            
            new_clothe = Clothes.objects.create(
                title=title,
                picture=picture,
                price=price,
                purchase_data=purchase_data,
                store=store_name,
                category=category_instance,
                user=request.user
            )
            
            messages.success(request, '服を登録しました。')
            return redirect('accounts:home')   
    else:
        create_clothe_form = forms.CreateClotheForm()
            
    return render(
        request, 'boards/create_clothe_form.html', context={
            'create_clothe_form': create_clothe_form,
        }
    )