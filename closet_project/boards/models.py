from django.db import models

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
    
    CATEGORY_CHOICES = [
        (BLOUSE, 'ブラウス'),
        (SHIRT, 'シャツ'),
        (SWEAT, 'スウェット'),
        (KNIT, 'ニット'),
        (PANTS, 'パンツ'),
        (SKIRT, 'スカート'),
        (JACKET, 'ジャケット'),
        (CARDIGAN, 'カーディガン'),
        (COAT, 'コート'),
        (DRESS, 'ドレス'),
        (SHOES, 'シューズ'),
        (ACCESSORY, 'アクセサリー'),
        (BAG, 'バッグ'),
    ]
    
    category_name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        
class Stores(models.Model):
   
    store_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'stores'

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
        
    COLOR_CHOICES = [
        (PINK, 'ピンク'),
        (RED, '赤'),
        (ORANGE, 'オレンジ'),
        (BROWN, '茶色'),
        (YELLOW, '黄色'),
        (BLUE, '青'),
        (GREEN, '緑'),
        (BLACK, '黒'),
        (WHITE, '白'),
    ]

    color_name = models.CharField(max_length=255, choices=COLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.color_name
    
    class Meta:
        db_table = 'colors'
    
class Clothes(models.Model):
    
    title = models.CharField(max_length=255)
    picture = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_data = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        'accounts.Users', on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Categories', on_delete=models.CASCADE
    )
    color = models.ManyToManyField(Colors)
    store = models.ForeignKey(
        'Stores', on_delete=models.CASCADE
    )
    
    def __str_(self):
        return self.title
    
    class Meta:
        db_table = 'clothes'