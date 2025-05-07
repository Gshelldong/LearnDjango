"""day53 URL Configuration

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
    # 无名分组会将括号中的内容传递给相应的函数,必须是一个分组才行
    re_path(r'^test/([0-9]{4})/', app01_views.test, name='app01_test'),
    re_path(r'^xxx/([0-9]{4})/', app01_views.xxx, name='xxx'),
    re_path(r'^test/(?P<year>\d+)/$', app01_views.test_named, name='app01_test_named'),

    # 多个具名分组的使用
    re_path(r'^date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', app01_views.nameds, name='app01_nameds')
]
