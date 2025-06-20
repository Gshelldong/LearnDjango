"""day58 URL Configuration

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
from app02 import views as app02_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('reg/', views.reg, name='reg'),
    path('lg/', app02_views.lg, name='lg'),
    path('home/', views.home, name='home'),
    path('loginout/', views.loginout, name='loginout'),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('detail/', views.detail, name='detail'),
]
