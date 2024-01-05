from django import forms
from .models import Categories,  Colors, Clothes 

    
class CreateClotheForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    picture = forms.FileField(label='写真', required=False)
    price = forms.IntegerField(label='価格',required=False)
    purchase_date = forms.DateTimeField(label='購入日', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(label='カテゴリー', queryset=Categories.objects.all())
    color = forms.ModelMultipleChoiceField(label='カラー', 
        queryset=Colors.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    store = forms.CharField(label='購入した店', required=False)
        
    class Meta:
        model=Clothes
        fields = ('title', 'picture', 'price', 'purchase_date', 'category', 'color', 'store')
        widgets = {
            'purchase_date': forms.DateInput(attrs={
                "type": "date"
            })
        }
        
class DeleteClotheForm(forms.ModelForm):
    pk = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = Clothes
        fields = []
       