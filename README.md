# LearnDjango
学习django框架使用的库

## cs与bs架构

1. 客户端   服务端
2. 浏览器   服务端
本质:bs也是cs

## HTTP协议

四大特性

1. 基于TCP/IP作用于应用层的协议
2. 基于请求响应
3. 无状态
    cookie,session,token
4. 无连接
    长连接:websocket


## 响应状态码

- 1XX
- 2XX
- 3XX
- 4XX
- 5XX



## 动静态网页
静态网页
	数据是写死的,万年不变
动态网页
	数据不是写死的 是动态获取到的
	比如:
		1.后端实时获取当前时间"传递"给前端页面展示
		2.后端从数据库获取数据"传递"给前端页面展示

传递给前端页面   >>>    页面渲染



## jinja2

```bash
pip3 install jinja2
```

由于flask框架是依赖于jinja2的 所以下载flask框架也会自带jinja2模块

模板的渲染 包含了 模板语法

模板语法(贴近python语法)
前端也能够使用后端的一些语法 操作后端传入的数据
```jinja2
# 渲染变量
<p>{{data}}</p>
<p>{{data['username']}}</p>
<p>{{data.password}}</p>
<p>{{data.get('hobby')}}</p>

# 循环展示
{%for user_dict in user_list%}
	<tr>
		<td>{{user_dict.id}}</td>
		<td>{{user_dict.name}}</td>
		<td>{{user_dict.password}}</td>
	</tr>
{%endfor%}

```


1.纯手撸web框架
	1.手动书写socket代码
	2.手动处理http数据

2.基于wsgiref模块帮助我们处理scoket以及http数据
	wsgiref模块
		1.请求来的时候 解析http数据 帮你打包成一个字典传输给你 便于你操作各项数据
		2.响应走的时候 自动帮你把数据再打包成符合http协议格式的样子 再返回给前端
		
3.封装路由与视图函数对应关系  以及视图函数文件网站用到的所有的html文件全部放在了
templates文件夹下
	1.urls.py 路由与视图函数对应关系
	2.views.py  视图函数(视图函数不单单指函数 也可以是类)
	3.templates  模板文件夹

4.基于jinja2实现模板的渲染
	模板的渲染
	后端生成好数据 通过某种方式传递给前端页面使用(前端页面可以基于模板语法更加快捷简便使用后端传过来的数据)


## Web框架
​	python三大主流web框架
​		1.Django:大而全 自带的功能特别特别多  就类似于航空母舰  有时候过于笨重
​		2.Flask:短小精悍  自带的功能特别特别少  全都是依赖于第三方组件
​			flask框架第三方的组件特别多 如果把flask第三方全部加起来  完全可以盖过Django
​			比较受限于第三方的开发者
​		3.Tornado:天生的异步非阻塞框架    速度特别快 能够抗住高并发
​			可以开发游戏服务器
​			
​		
​		A:socket
​		B:路由与视图函数匹配
​		C:模板语法


​		
​		Django
​			A:用的别人的 wsgiref
​			B:自己写的
​			C:自己写的  
​		Flask
​			A:用的别人的 wsgiref>>> werkzeug
​			B:自己写的
​			C:用的别人的 jinja2
​		Tornado
​			A,B,C全都是自己写的
​		
## Django

![image-20250411140753625](images/image-20250411140753625.png)

​	注意事项
​		1.你的计算机的名称不能有中文
​		2.文件的命名尽量也不要用中文
​		3.一个pycharm窗口只能有一个项目 不要把多个项目放在一个窗口下
​		
​	
​	django版本问题
​		1.x  2.x
​		
​		以django1.11版本为主
​	django下载
​		pip3 install django==1.11.11
​	如何确认是否下载成功
​		命令行敲 django-admin


## 如何创建django项目
命令行式
1.命令行创建django项目
```python
django-admin startproject 项目名
```

2.命令行创建django应用(一个应用对应一块儿独立的功能)

```python
django-admin startapp 应用名
python manage.py startapp 应用名
```

3.命令行启动django项目

```ptyhon
python manage.py runserver
```

	(******)
	注意 用命令行创建django项目  不会自动新建templates模板文件夹
	需要你自己手动创建 并且需要你自己去settings.py文件中注册该文件路径
**创建的应用一定要在settings中注册才能生效否则无法识别**

```python
# settings.py

		INSTALLED_APPS = [
				'django.contrib.admin',
				'django.contrib.auth',
				'django.contrib.contenttypes',
				'django.contrib.sessions',
				'django.contrib.messages',
				'django.contrib.staticfiles',
				# 'app01'  # 简写
				'app01.apps.App01Config'  # 全称
			]
```



## django主要文件介绍

```bash
项目名文件
	同名的项目文件夹
		settings.py  django暴露给用户可配置的文件
		urls.py      路由与视图函数对应关系
	manage.py  django入口文件
	应用文件夹
		migrations文件夹   数据库迁移记录
		admin.py  django后台管理
		apps.py   应用注册相关
		models.py  orm模型类
		tests.py   测试文件
		views.py   视图函数
```

##　django小白必会三板斧

HttpResponse: 返回字符串
render: 返回html页面 并且能够给该页面传值
redirect: 重定向

## 静态配置文件

html文件默认全都放在templates文件夹下
对于前段已经写好了的文件 我们只是拿过来使用 那么这些文件都可以称之为叫"静态文件"
静态文件可以是

- bootstrap一类的前段框架 已经写好了的
- 图片
- css
- js

静态文件默认全都放在static文件夹下，static文件夹中默认会默认创建的子文件夹
- css文件夹  当前网站所有的样式文件
- js文件  当前网站所有的js文件
- img文件  当前网站所有的图片文件
- 其他(前端框架代码 第三方插件代码...)

**用户可以访问的资源都在url中只有url中开设相关的资源你才能访问到**
后端资源一般都需要手动指定是否需要暴露给用户
	
静态文件配置

```python
# settings.py
STATICFILES_DIRS = [
		os.path.join(BASE_DIR,'static')
]
```

你只要输入static文件夹内具体文件的路径就能够访问到
静态文件是从上向下加载,加载到满足条件的就停止。

```python
# 这个static不是文件夹的名字 而是接口前缀
# 只要你想访问静态文件中的资源 文件路径就必须用static开头
# settings.py
STATIC_URL = '/static/'  

# 手动将static文件夹中所有的资源暴露给用户
STATICFILES_DIRS = [
	os.path.join(BASE_DIR,'static'),  # 真正的文件夹路径
	os.path.join(BASE_DIR,'static1'),  # 真正的文件夹路径
	os.path.join(BASE_DIR,'static2'),  # 真正的文件夹路径
	os.path.join(BASE_DIR,'static3')  # 真正的文件夹路径
]
```

django默认是支持自动重启代码的所以你只需要多刷新几次页面就可以
但是有时候它的重启机制比较慢
- 机制:实时监测文件代码变化只要有变化就会自动重启 
- 可能你的代码还没有写完这个时候就会自动报错


静态文件接口前缀"动态解析"
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
    <script src="{% static 'jquery-3.7.1.min.js' %}"></script>
    <link rel="stylesheet" href="{% static 'bootstrap-3.4.1-dist/css/bootstrap.min.css' %}">
    <script src="{% static 'bootstrap-3.4.1-dist/js/bootstrap.min.js' %}"></script>
    <link rel="stylesheet" href="https://lf3-cdn-tos.bytecdntp.com/cdn/expire-1-M/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
```



## 获取表单内容

form表单默认是get请求
携带数据的方式是url问好后跟数据
http://127.0.0.1:8000/login/?username=zekai&password=123
	
可以通过前面input标签中的属性method改为post请求
改成post请求之后需要去settings文件中注释掉一个中间件，这样设置可以跳过浏览器生成的cookie

```python
# settings.py
		MIDDLEWARE = [
			'django.middleware.security.SecurityMiddleware',
			'django.contrib.sessions.middleware.SessionMiddleware',
			'django.middleware.common.CommonMiddleware',
			# 'django.middleware.csrf.CsrfViewMiddleware',
			'django.contrib.auth.middleware.AuthenticationMiddleware',
			'django.contrib.messages.middleware.MessageMiddleware',
			'django.middleware.clickjacking.XFrameOptionsMiddleware',
		]
```

form表单提交数据目的地由action属性决定

		1. 不写的情况下 默认往当前地址提交
		2. 还可以写后缀/index/(将项目常用这种)
		3. 还可以写全路径

视图函数一般主要会先处理get请求

```python
def login(request):
	# 视图函数针对不同的请求方式 应该有不同的处理逻辑
	# if request.method == 'GET':
	#     print('收到了')
	#     print(request.method)  # 能够获取前端请求方式 并且是全大写的字符串
	#     print(type(request.method))
	#     return render(request,'login.html')
	# elif request.method == 'POST':
	#     # 获取用户输入 做相应的逻辑判断
	#     return HttpResponse("拿到了 老弟")
    # 针对POST方法做单独的处理，用户提交表单了，这样代码逻辑更加清晰，其它请求直接返回
	if request.method == 'POST':
		return HttpResponse('来啦 宝贝')
	return render(request,'login.html')
```

### 获取前端数据
request.method 获取请求方法

对数据的处理不单单只有wsgiref模块django后端也进行了大量的数据处理

在视图函数中request有wsgiref和django的处理，要查看request携带的详细信息，可以通过IDE debug的方式查看

GET

```python
# 获取前端get提交的数据(就类似于是一个大字典)
request.GET 
        # 取值
        # 虽然value是一个列表但是默认只取列表最后一个元素
        # 强烈不建议你使用中括号的形式取值
    	request.GET.get('username')
    	
    	# 如果想直接把列表全部取出(***重要***)
        # 推荐使用这种方式，如果同一个字段有多个值的情况就可以全部取到，然后再进行处理
    	request.GET.getlist('hobby')
```

POST
```python
# 获取前端post提交的数据(就类似于是一个大字典)
request.POST 
    # 取值
    # 虽然value是一个列表 但是默认只取列表最后一个元素
    # 强烈不建议你使用中括号的形式取值
	request.POST.get('username') 
	
	# 如果想直接把列表全部取出(******)
	request.POST.getlist('hobby')
```


## django 连接数据库

django默认使用的是自带的sqlite数据库 
如果你想让它其他的数据库需要在settings配置文件中配置
1.settings文件中配置

```python
# settings.py 
        DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'day51', # 数据名称
        'HOST':'127.0.0.1',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'123',
        'CHARSET':'utf8'
    }
```

2.还要在项目名下或者是app名下的`__init__.py`文件中告诉django不要使用默认的mysqldb,而是使用pymysql

```python
import pymysql
pymysql.install_as_MySQLdb()
```
## django ORM

### ORM对象关系映射

| 表           | 类           |
| ------------ | ------------ |
| 一条条记录   | 对象         |
| 字段对应的值 | 对象属性属性 |


首先需要在应用下的models.py中书写模型类
```python
class User(models.Model):
	# 将id字段设置为User表主键字段  在django orm中 你可以不写主键字典  django会默认给你的表创建一个名为id的主键字段
	# id = models.AutoField(primary_key=True)  # 一旦你自己指定了主键字段 那么django就不会自动再帮你创建了
	username = models.CharField(max_length=32)  # username varchar(32)   CharField必须要指定max_length参数
	password = models.IntegerField()  # password int
```
| 字段                                        | mysql中的类型                     |
| ------------------------------------------- | --------------------------------- |
| CharField(max_length=32)                    | varchar(32)                       |
| IntegerField                                | int                               |
| IntegerField(null=True)                     | 允许为空                          |
| CharField(max_length=32, default='China')   | 默认值china                       |
| DecimalField(max_digits=8,decimal_places=2) | 浮点型，总共8位，保留小数点后两位 |
|                                             |                                   |

**需要执行数据库迁移(同步)命令**,只要修改了模型就必须这样修改。

```python
# 仅仅是在小本本上(migrations文件夹)记录数据库的修改 并不会直接操作数据
python3 manage.py makemigrations

# 将数据库修改记录 真正同步到数据库
python3 manage.py migrate

注意:只要动了models中跟数据库相关的代码就必须重新执行上面的两条命令缺一不可(******)

```

实际上只生成了一个app01_user的表，加上一个app01的前缀可以区分每个不同app中有相同名称的表重复，其它的表都是django生成的表。

![image-20250411144434048](images/image-20250411144434048.png)

### 表字段的增删改查

**注意:只要动了models中跟数据库相关的代码 就必须重新执行上面的两条命令缺一不可**

增
```python
# 当一张表已经创建出来之后 后续还想添加字段,可以有两种方式
# 1.给新增的字段设置默认值
	addr = models.CharField(max_length=32,default='China')  # default该字段默认值
# 2.给新增的字段设置成可以为空
	age = models.IntegerField(null=True)  # 该字段允许为空
```

删(慎用)

- 删除字段直接在models.py中注释该字段然后重新执行两条命令即可
- 注意:执行完之后 表中该字段所对应的所有的数据全部删除
- 并且一般情况下 基本是不会用到真正意义上的删除


orm操作需要使用models中的类的名字

### 数据操作

查数据有两种方法`get`和`filter`数据库中没有get的数据的时候，代码会报错，所以推荐使用filter的方式。

```python
from app01 import models

models.User.objects.all()  # 直接拿所有的数据

models.User.objects.get(username=username)  

res = models.User.objects.filter(username=username)
res.query 

user_obj = res.first()
```

数据的增
```python
1.
models.User.objects.create(username=username,password=password)
# 2.save方法会更新全部字段的内容，即使是只修改了一个字段。
user_obj = models.User(username=username,password=password)
user_obj.save()
```

删
```python
models.User.objects.filter(条件).delete()
```

改
```python
# 推荐使用update方法
models.User.objects.filter(条件).update('key'='value')

        filter拿到是一个列表,filter操作其实都是批量操作
        如果filter结果列表中有多个数据那么会一次性全部修改 
        类似于for循环一个个修改.
        
# 方式二(不推荐使用)
edit_obj.username = username
edit_obj.password = password
edit_obj.save()
"""
第二种方式会从头到尾将所有的字段全部修改一遍  效率极低
"""
```

用户的增删改查
1.通过orm展示所有的到前端
	all()
	模板语法for循环



2.添加新增按钮 (用户的新增操作)
	a标签的href直接触发后端逻辑
	create()



3.添加编辑 删除按钮
	编辑
	删除
		利用get请求携带参数的特点  在url的后面跟上对应数据的id值
		request.GET.get()

如果是编辑 
	重新渲染一个页面 将编辑对象传递到前端

如果是删除
	直接利用filter(...).delete()



图书管理系统表关系设计

![image-20250421153839544](images\image-20250421153839544.png)

多对多：书和出版社联合出版，一个出版社出版多本书。

一对多：一个作者出版多本书。

一对一：用户和用户详情，用户的唯一id对应用的详情表。

### 表与表之间建立联系

django orm中表与表之间建关系。

多对多会建立第三张表去做中间的映射。to后面的是表的名字。默认情况下会与表的主键id相关联。

|        |                                  |
| ------ | -------------------------------- |
| 一对多 | ForeignKey(to='Publish')         |
| 一对一 | OneToOneField(to='AuthorDetail') |
| 多对多 | ManyToManyField(to='Author')     |
|        |                                  |

使用方式：

```python

```

注意:
前面两个关键字会自动再字段后面加_id
最后一个关键字 并不会产生实际字段 只是告诉django orm自动创建第三张表。

## 路由层urls.py

url()方法第一个参数其实是一个正则表达式一旦前面的正则匹配到了内容就不会再往下继续匹配而是直接执行对应的视图函数正是由于上面的特性当你的项目特别庞大的时候url的前后顺序也是你需要你考虑极有可能会出现url错乱的情况。

django在路由的匹配的时候，当你在浏览器中没有敲最后的斜杠django会先拿着你没有敲斜杠的结果取匹配如果都没有匹配上，会让浏览器在末尾加斜杠再发一次请求再匹配一次，如果还匹配不上才会报错。

如果你想取消该机制不想做二次匹配可以在settings配置文件中指定:
```bash
APPEND_SLASH = False  # 该参数默认是True
```

django3.2版本中使用的是

```bash
from django.urls import re_path

urlpatterns = [
    re_path(r'^articles/(?P<year>\d+)/$', views.year_archive),
]
```



### 无名分组

必须是一个分组才行。

```python
urls     url(r'^test/([0-9]{4})/', views.test)
# 路由匹配的时候会将括号内正则表达式匹配到的内容当做位置参数传递给视图函数。
views    test(request,2019)
```

### 有名分组

```python
urls		url(r'^test/(?P<year>\d+)/', views.test)
# 路由匹配的时候会将括号内正则表达式匹配到的内容当做关键字参数传递给视图函数
views		test(request,year=2019)
```

注意：无名有名不能混合使用 !!!

同一种分组可以重复使用。

```python
# 无名分组支持多个
# url(r'^test/(\d+)/(\d+)/', views.test),
# 有名分组支持多个
# url(r'^test/(?P<year>\d+)/(?P<xx>\d+)/', views.test),
```

### 反向解析

本质:其实就是给你返回一个能够返回对应url的地址
		
1.先给url和视图函数对应关系起别名

```python
url(r'^index/$',views.index,name='kkk')
```

2.反向解析
后端反向解析,后端可以在任意位置通过reverse反向解析出对应的url
```python
from django.shortcuts import render,HttpResponse,redirect,reverse

def xxx(request):
    print(reverse('kkk'))
    
# 前端反向解析
	{% url 'kkk' %}
```

### 无名分组反向解析

```python
url(r'^index/(\d+)/$',views.index,name='kkk')

# 后端反向解析
	reverse('kkk',args=(1,))  # 后面的数字通常都是数据的id值
# 前端反向解析
	{% url 'kkk' 1%}   # 后面的数字通常都是数据的id值
```

### 有名分组反向解析

同无名分组反向解析意义的用法		

```python
url(r'^index/(?P<year>\d+)/$',views.index,name='kkk')
		
后端方向解析
print(reverse('kkk',args=(1,)))  # 推荐你使用上面这种减少你的脑容量消耗
print(reverse('kkk',kwargs={'year':1}))

前端反向解析

<a href="{% url 'kkk' 1 %}">1</a>  # 推荐你使用上面这种减少你的脑容量消耗
<a href="{% url 'kkk' year=1 %}">1</a>
```
注意:在同一个应用下别名千万不能重复!!!
