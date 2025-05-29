"""library_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views as app01_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', app01_views.home, name='app01_views'),
    path('listbook/', app01_views.list_book, name='listbook'),
    path('addbook/', app01_views.add_book, name='addbook'),
    path('user/', app01_views.user, name='user'),
    re_path('^edit_book/(?P<edit_id>\d+)', app01_views.edit_book, name='edit'),
    re_path('^delete_book/(?P<delete_id>\d+)', app01_views.delete_book, name='delete'),
]
