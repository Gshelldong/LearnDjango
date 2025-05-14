from django.urls import path,re_path
from app01 import views


app_name = 'app01'
urlpatterns = [
    path('index/', views.list_book, name='app01_list'),
]