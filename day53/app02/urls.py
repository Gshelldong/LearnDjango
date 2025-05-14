from django.urls import path,re_path
from app02 import views

app_name = 'app02'
urlpatterns = [
    path('index/', views.app02_index, name='app02_index'),
]