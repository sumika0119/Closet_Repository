from django.contrib import admin
from django.urls import path
from .views import CustomLoginView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),  # admin画面のURL設定
    path('', views.home, name='home'),
    path('regist', views.regist, name='regist'),
    path('activate_user/<uuid:token>', views.activate_user, name='activate_user'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_edit', views.user_edit, name='user_edit'),
    path('change_password', views.change_password, name='change_password'),
]