from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from django.utils import timezone
from django.utils.timezone import timedelta

from django.urls import reverse_lazy
from django.contrib import admin

        
class UserManager(BaseUserManager):
        
    def _create_user(self, username, email, password):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise ValueError('Superuser must have a password')

        user = self._create_user(username, email, password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'

class UserActivateTokensManager(models.Manager):    
   
    def activate_user_by_token(self, token):
        user_activate_token = UserActivateTokens.objects.filter(
            token=token,
            expired_at__gte=timezone.now()
        ).first()
        if user_activate_token:
            user = user_activate_token.user
            user.is_active = True
            user.save()
            return user
        return None
        
class UserActivateTokens(models.Model):
    
    token = models.UUIDField(db_index=True)
    expired_at =models.DateTimeField()
    user = models.ForeignKey(
        'Users', on_delete=models.CASCADE
    )
    
    objects = UserActivateTokensManager()
    
    class Meta:
        db_table = 'user_activate_tokens'
          
   
        
@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
    print("Post save signal called")
    user_activate_token = UserActivateTokens.objects.create(
        user=instance, token=str(uuid4()), expired_at=timezone.now() + timedelta(days=1)
    )
    print(f"Token: {user_activate_token.token}, Expired At: {user_activate_token.expired_at}")
