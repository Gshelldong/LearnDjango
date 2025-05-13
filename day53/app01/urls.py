from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('app01/', views.list_book, name='app01_list'),
]