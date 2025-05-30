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
from django.urls import path,re_path,include
from app01 import views as app01_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^index/(\d+)/', app01_views.index, name='app01_index'),
    path('login/', app01_views.login, name='app01_login'),
    path('testadd/',app01_views.testadd, name='testadd'),
    # 无名分组会将括号中的内容传递给相应的函数,必须是一个分组才行
    # re_path(r'^test/([0-9]{4})/', app01_views.test, name='app01_test'),
    re_path(r'^xxx/([0-9]{4})/', app01_views.xxx, name='xxx'),
    re_path(r'^test/(?P<year>\d+)/$', app01_views.test_named, name='app01_test_named'),

    # 多个具名分组的使用
    re_path(r'^date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', app01_views.nameds, name='app01_nameds'),

    # 书籍管理的路由
    path('book_infoo/', app01_views.list_book, name='book_info'),
    path('add_book/', app01_views.add_book, name='add_book'),
    re_path(r'del_book/(?P<id>\d+)', app01_views.del_book, name='del_book'),
    re_path(r'edit_book/(?P<id>\d+)', app01_views.edit_book, name='edit_book'),

    path(r'app02/',include('app02.urls', namespace='app02')),
    path(r'app01/',include('app01.urls', namespace='app01')),

    path(r'pipei/<int:num>/', app01_views.pipei, name='pipei'),

    path(r'json/',app01_views.return_json,name='app_json'),
    path(r'up/',app01_views.upload_file,name='up'),
]
