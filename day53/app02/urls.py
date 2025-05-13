from django.urls import path,re_path
from app02 import views

urlpatterns = [
    path('app02/', views.app02_index, name='app02_index'),
]