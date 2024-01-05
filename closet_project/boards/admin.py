from django.contrib import admin
from .models import (Categories, Colors, Clothe_Colors, Clothes)
# Register your models here.


admin.site.register(
    [Categories, Colors, Clothe_Colors, Clothes]
)