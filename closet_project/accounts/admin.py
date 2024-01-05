from django.contrib import admin
from .models import Users
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff','is_superuser')
    form = CustomUserChangeForm
    
admin.site.register(Users, UsersAdmin)