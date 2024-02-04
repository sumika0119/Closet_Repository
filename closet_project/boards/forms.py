from django import forms
from .models import Categories,  Colors, Clothes 

    
class CreateClotheForm(forms.ModelForm):
    title = forms.CharField(label='タイトル', required=True)
    picture = forms.FileField(label='写真', required=False)
    price = forms.IntegerField(label='価格',required=False)
    purchase_date = forms.DateField(label='購入日', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    category = forms.ModelChoiceField(label='カテゴリー', queryset=Categories.objects.all())
    color = forms.ModelMultipleChoiceField(label='カラー', 
        queryset=Colors.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    store = forms.CharField(label='購入した店', required=False)
        
    def __init__(self, *args, **kwargs):
       
        categories = kwargs.pop('categories', None)
        colors = kwargs.pop('colors', None)
        instance = kwargs.get('instance')
        super(CreateClotheForm, self).__init__(*args, **kwargs)

        if categories:
            self.fields['category'].queryset = categories

        if colors:
            self.fields['color'].queryset = colors
            
        existing_colors = instance.color.values_list('id', flat=True) if instance and instance.color.exists() else []
        self.initial['color'] = existing_colors
            
            
            
    class Meta:
        model=Clothes
        fields = ('title', 'picture', 'price', 'purchase_date', 'category', 'color', 'store')
        widgets = {
        'title': forms.TextInput(attrs={'required': True}),
        'category': forms.Select(attrs={'required': True}),
        'color': forms.CheckboxSelectMultiple(attrs={'required': True}),
        'purchase_date': forms.DateInput(attrs={'type': 'date', 'required': True}),
    }
        error_messages = {
            'title': {
                'required': 'タイトルを入力してください。',
            },
            'category': {
                'required': 'カテゴリーを選択してください。',
            },
            'color': {
                'required': 'カラーを選択してください。',
            },
        }
        
class DeleteClotheForm(forms.ModelForm):
    pk = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = Clothes
        fields = []
       