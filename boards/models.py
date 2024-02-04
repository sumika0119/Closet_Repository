from django.db import models
from accounts.models import Users

# Create your models here.
class Categories(models.Model):
    
    BLOUSE = 'blouse'
    SHIRT = 'shirt'
    SWEAT = 'sweat'
    KNIT = 'knit'
    PANTS = 'pants'
    SKIRT = 'skirt'
    JACKET = 'jacket'
    CARDIGAN = 'cardigan'
    COAT = 'coat'
    DRESS = 'dress'
    SHOES = 'shoes'
    ACCESSORY = 'accessory'
    BAG = 'bag'
    
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        
    def __str__(self):
        return self.category_name
        
        
# class Stores(models.Model):
   
#     store_name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         db_table = 'stores'

class Colors(models.Model):
    
    PINK = 'pink'
    RED = 'red'
    ORANGE = 'orange'
    BROWN = 'brown'
    YELLOW = 'yellow'
    BLUE = 'blue'
    GREEN = 'green'
    BLACK = 'black'    
    WHITE = 'white'
        
    color_name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.color_name
    
    class Meta:
        db_table = 'colors'
    
class ClothesManager(models.Manager):
    def fetch_all_clothe(self):
        return self.all()


class Clothes(models.Model):
    
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='closet_project/media/', null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    purchase_date = models.DateField(null=True,blank=True)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Categories', on_delete=models.CASCADE
    )
    color = models.ManyToManyField(
        Colors, blank=True, through='Clothe_Colors', related_name='clothe'
    )
    store = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ClothesManager()
    
    class Meta:
        db_table = 'clothes'
        
    def __str__(self):
        return self.title
    
class Clothe_Colors(models.Model):
    clothe = models.ForeignKey(
        Clothes, on_delete=models.CASCADE, related_name='clothe_color_relation',
    )
    color = models.ForeignKey(
        Colors, on_delete=models.CASCADE, related_name='color_clothe_relation',
    )