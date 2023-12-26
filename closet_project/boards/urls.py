from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create_clothe', views.create_clothe, name='create_clothe'),
]