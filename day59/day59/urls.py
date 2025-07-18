"""day59 URL Configuration

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
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('pay/',views.pay, name='pay'),
    path('auth_login/',views.auth_login, name='auth_login'),
    path('is_login/',views.is_login, name='is_login'),
    path('user_detail/',views.user_detail, name='user_detail'),
    path('alter_password/',views.alter_password, name='alter_password'),
    path('register/',views.register, name='register'),
]
