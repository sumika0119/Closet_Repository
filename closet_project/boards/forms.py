from django import forms
from .models import Categories, Stores, Colors, Clothes 


class CreateClotheForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    picture = forms.ImageField(label='写真')
    price = forms.DecimalField(label='価格')
    purchase_data = forms.DateTimeField(label='購入日')
    category = forms.ChoiceField(label='カテゴリー', choices=Categories.CATEGORY_CHOICES)
    color = forms.ChoiceField(label='カラー', choices=Colors.COLOR_CHOICES)
    store = forms.CharField(label='購入した店')
        
    class Meta:
        model=Clothes
        fields = ('title', 'picture', 'price', 'purchase_data', 'category', 'store')
        