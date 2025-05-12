from django.urls import path,re_path



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
]