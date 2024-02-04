from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create_clothe', views.create_clothe, name='create_clothe'),
    path('list_clothe', views.list_clothe, name='list_clothe'),
    path('detail_clothe/<int:pk>/', views.detail_clothe, name='detail_clothe'),
    path('edit_clothe/<int:pk>/', views.edit_clothe, name='edit_clothe'),
    path('delete_clothe/<int:pk>/', views.delete_clothe, name='delete_clothe'),
    path('delete_clothe_complete/', views.delete_clothe_complete, name='delete_clothe_complete'),
]