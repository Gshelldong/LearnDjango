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

## MTV与MVC模型

django框架自称为是MTV框架

> M:models
> T:templates
> V:views 

MVC

> M:models
> V:views
> C:controller 控制器(urls)


本质:MTV其实也是MVC

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
`request.method`获取请求方法

对数据的处理不单单只有wsgiref模块django后端也进行了大量的数据处理

在视图函数中request有wsgiref和django的处理，要查看request携带的详细信息，可以通过IDE debug的方式查看

**GET**

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

**POST**

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
## [day53]()

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
| 字段                                        | mysql中的类型                                                |
| ------------------------------------------- | ------------------------------------------------------------ |
| CharField(max_length=32)                    | varchar(32)                                                  |
| IntegerField                                | int                                                          |
| IntegerField(null=True)                     | 允许为空                                                     |
| CharField(max_length=32, default='China')   | 默认值china                                                  |
| DecimalField(max_digits=8,decimal_places=2) | 浮点型，总共8位，保留小数点后两位                            |
| EmailField()                                | 就是varchar(254)                                             |
| DateField()                                 | 年月日                                                       |
| DateTimeField()                             | 年月日-时分秒 auto_now m每次修改都会更新时间<br />auto_now_add只有在创建的时候生成 |
| BooleanField()                              | orm中的布尔值，数据库中存的是0和1                            |
| TextField()                                 | 文本类型                                                     |
| FileField(Filed)                            | 字符串， 文件路径保存到数据库；如果指定了upload_to=参数会把上传的文件直接放在对应的目录下。 |
| FloadField()                                | 浮点型                                                       |

unique=True 是否是唯一的

db_index=True 为该字段0添加索引

on_delete 关联字段，删除关联数据时的关联行为。

#### 自定义字段

```python
class MyChar(models.Field):
    def __init__(self,max_length,*args,**kwargs):
        self.max_length = max_length
        super().__init__(max_length=max_length,*args,**kwargs)
        
    def db_type(self, connection):
        return  'char(%s)'%self.max_length
```

#### choice字段

比如性别字段在数据库中存储不会直接存储男或者女而是使用数字来代替，在orm中可以使用choice字段声明。orm在查询的时候使用内置方法直接进行映射关系的查询。实际上只是代码中的声明，在数据库中并不会限制字段的值。

```python
# 如果没有对应关系的字段，就会直接打印原来的值
class User(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    choice = [
        (1,'男'),
        (2,'女'),
        (3,'其它'),
    ]
    gender = models.IntegerField(choices=choice)

# 数据库中表的定义
CREATE TABLE `app01_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` int(11) NOT NULL, # 没有限制只能选择哪些值
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

# 查询的结果
res = models.User.objects.filter(pk=1).first() # type: models.User
print(res.get_gender_display()) # -> 男
```



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

### 多对多创建的三种方式

#### 1.全自动

**推荐使用**

- 优势：不需要手动创建第三张表。
- 不足：由于第三张表不是你手动创建的，也就意味着第三张表字段是固定的无法扩展。

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to='Author')
    publication_date = models.DateField()
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name
```

#### 2.纯手动(了解)

自己创建第三张表。

优势：第三张表可以扩展任意字段。

不足：ORM查询不方便。

```python
class Book(models.Model):
	title = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=8,decimal_places=2)

class Author(models.Model):
	name = models.CharField(max_length=32)

class Book2Author(models.Model):
	book = models.ForeignKey(to='Book')
	author = models.ForeignKey(to='Author')
	create_time = models.DateField(auto_now_add=True)
```

#### 3.半自动(推荐使用)

优势:结合了全自动和纯手动的两个优点

不足：不支持多对多内置方法的查询。

- add
- set
- remove
- clear

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to='Author', through='BooktoAuthor', through_fields=('book', 'author'))
    publication_date = models.DateField()
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(to='Book', through='BooktoAuthor', through_fields=('author', 'book'))
    # through 告诉django orm书籍表和作者表的多对多关系是通过BooktoAuthor来记录的
    # through_fields 告诉django orm记录关系时用过BooktoAuthor表中的book字段和author字段来记录的
    email = models.EmailField()
    def __str__(self):
        return self.name

class BooktoAuthor(models.Model):
    book = models.ForeignKey(to='Book',on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author',on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.book.title} - {self.author.name}'
```





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

### 批量插入数据

```python
bulk_create()  批量插入数据

# for i in range(1000):
#     models.Book.objects.create(title='第%s本书'%i)
# 上面这种方式 效率极低

l = []
for i in range(10000):
	l.append(models.Book(title='第%s本书'%i))
models.Book.objects.bulk_create(l)  # 批量插入数据
```

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

默认路由

```python
r'^$'
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

本质:其实就是给你返回一个能够返回对应url的地址，就是给路由一个别名，在`urls.py`修改了路由之后，前端或者后端都能够通过别名来把修改的部分解析出来。
		
1.先给url和视图函数对应关系起别名

```python
url(r'^index/$',views.index,name='kkk')
```

2.反向解析
后端反向解析，后端可以在任意位置通过reverse反向解析出对应的url；前提是函数需要满足接收正则匹配到的参数，如果正则中有分组信息，但是函数中没有分组，就报导致函数传参错误。

### 无分组信息的反向解析

```python
from django.shortcuts import render,HttpResponse,redirect,reverse

def xxx(request):
    print(reverse('kkk'))
    
# 前端反向解析，从url中的kkk别名中来的
	{% url 'kkk' %}

path('index111/', app01_views.index, name='app01_index'),
# 这里会把href中的链接直接解析为index111/所以无论后端如何修改，前端的url也会跟着修改
<a href="{% url 'app01_index' %}">index9</a>
```

### 无名分组反向解析

```python
url(r'^index/(\d+)/$',views.index,name='kkk')

# 后端反向解析
	reverse('kkk',args=(1,))  # 后面的数字通常都是数据的id值
# 前端反向解析
	{% url 'kkk' 1%}   # 后面的数字通常都是数据的id值

# 无名分组的使用和写法
# urls
re_path('^index/(\d+)/', app01_views.index, name='app01_index'),

# views
def index(request,*args):
    # 注意这里渲染的始终是一个容器如列表，元祖等
    print(reverse('app01_index',args=args))
    return render(request, 'index.html')

# index.html
<body>
<a href="{% url 'app01_index' 1%}123/">index2</a>
<a href="{% url 'app01_index' 123%}456/">index3</a>
</body>
```

实际使用场景编辑用户对id的渲染

```python
"""
url(r'^edit_user/(\d+)/',views.edit_user,name='aaa'),

{% for edit_obj in edit_list%}
<a href="edit_user/{{edit_obj.id}}/">编辑</a>
{%endfor%}

def edit_user(request,edit_id):
    reverse('aaa',args=(edit_id,))
```

### 有名分组反向解析

同无名分组反向解析意义的用法		

```python
url(r'^index/(?P<year>\d+)/$',views.index,name='kkk')
		
# 后端方向解析
print(reverse('kkk',args=(1,)))  # 推荐你使用上面这种减少你的脑容量消耗
print(reverse('kkk',kwargs={'year':1}))

前端反向解析

<a href="{% url 'kkk' 1 %}">1</a>  # 推荐你使用上面这种减少你的脑容量消耗
<a href="{% url 'kkk' year=1 %}">1</a>
```

```python
# 换种写法urls.py
re_path(r'^test/(?P<year>\d+)/$', app01_views.test_named, name='app01_test_named'),

# views.py
def test_named(request, year=None):
    print(year)
    return HttpResponse('uri number is {}'.format(year))

# 匹配的结果
/test/2025/
```

```python
# 这里在定义了之后同样会打印定义的值
# views.py
def test_named(request, year=None):
    print(year)
    print('rev: ', reverse('app01_test_named', kwargs={'year': 2029}))
    return HttpResponse('uri number is {}'.format(year))

rev:  /test/2029/
```
注意:在同一个应用下别名千万不能重复!!!

### 路由分发

当你的django项目特别庞大的时候,路由与视图函数对应关系特别特别多。
那么你的总路由urls.py代码太过冗长不易维护。
`每一个应用都可以有自己的urls.py,static文件夹,templates文件夹`
正是基于上述条件可以实现多人分组开发等多人开发完成之后我们只需要创建一个空的django项目，然后将多人开发的app全部注册进来在总路由实现一个路由分发而不再做路由匹配(来了之后 我只给你分发到对应的app中)。
当你的应用下的视图函数特别特别多的时候你可以建一个views文件夹里面根据功能的细分再建不同的py文件(******)

```python
# 在urls.py中导别名，include中就可以直接写as的别名
from app01 import views as app01_views
from app02 import views as app02_views

# 主urls.py
        urlpatterns = [
			url(r'^admin/', admin.site.urls),
            # 推荐使用这种用法
			url(r'^app01/',include('app01.urls')),
			url(r'^app02/',include('app02.urls')),
		]
    
# app01 urls.py
urlpatterns = [
    path('index/', views.list_book, name='app01_list'),
]

# app02 urls.py
urlpatterns = [
    path('index/', views.app02_index, name='app02_index'),
]
```

### 名称空间

给每个app的url.py中一个名称，然后名称空间中引用。

多个app起了相同的别名 这个时候用反向解析 并不会自动识别应用前缀。
如果想避免这种问题的发生。

```bash
方式1:
	总路由，总路由中一级路由的后面千万不加$符号
		url(r'^app01/',include('app01.urls',namespace='app01'))
		url(r'^app02/',include('app02.urls',namespace='app02'))
	后端解析的时候
		reverse('app01:index')
		reverse('app02:index')
	前端解析的时候
		{% url 'app01:index' %}
		{% url 'app02:index' %}

方式2: 不使用名称空间:
	起别名的时候不要冲突即可一般情况下在起别名的时候通常建议以应用名作为前缀
		name = 'app01_index'
		name = 'app02_index'
```

django 3.2版本的配置

```python
# 主urls.py中配置
    path(r'app02/',include('app02.urls', namespace='app02')),
    path(r'app01/',include('app01.urls', namespace='app01')),
    
# app01 urls.py的配置
    # 必须定义app_name，就是主路由中定义的namespace
	app_name = 'app01'
    urlpatterns = [
        path('index/', views.list_book, name='app01_list'),
    ]
    
# app02 urls.py的配置
    app_name = 'app01'
    urlpatterns = [
        path('index/', views.list_book, name='app01_list'),
    ]
```

## 伪静态

静态网页:数据是写死的万年不变。

伪静态网页的设计是为了增加百度等搜索引擎seo查询力度。

所有的搜索引擎其实都是一个巨大的爬虫程序。

网站优化相关 通过伪静态确实可以提高你的网站被查询出来的概率。

## 虚拟环境

一般情况下我们会给每一个项目配备该项目所需要的模块不需要的一概不装虚拟环境就类似于为个项目量身定做的解释器环境。
每创建一个虚拟环境就类似于你又下载了一个全新的python解释器。

## django版本路由的区别

### django1.X跟django2.X版本区别
路由层1.X用的是url,而2.X用的是path

2.X中的path第一个参数不再是正则表达式,而是写什么就匹配什么 是精准匹配

当你使用2.X不习惯的时候 ,2.X还有一个叫re_path
2.x中的re_path就是你1.X的url


虽然2.X中path不支持正则表达式  但是它提供了五种默认的转换器

1.0版本的url和2.0版本的re_path分组出来的数据都是字符串类型。
默认有五个转换器，感兴趣的自己可以课下去试一下

- str,匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
- int,匹配正整数，包含0。
- slug,匹配字母、数字以及横杠、下划线组成的字符串。
- uuid,匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
- path,匹配任何非空字符串，包含了路径分隔符（/）（不能用？）



```python
path('index/<int:id>/',index)  # 会将id匹配到的内容自动转换成整型
```

访问 /index/12346  id传到后端是一个kv的形式传递到后端的`id=123456`所以后端接收要么接收任意关键字参数要么接收，位置参数`id`

```python
# urls.py
path(r'pipei/<int:num>/', app01_views.pipei, name='pipei'),

# 处理的函数
def pipei(request,**kwargs):
    print(kwargs)
    return HttpResponse(b'hello baby')

# 方式二：
def pipei(request,num):
    print(num)
    return HttpResponse(b'hello baby')
```



### 自定义转换器

```python
class FourDigitYearConverter:  
regex = '[0-9]{4}'  
def to_python(self, value):  
	return int(value)  
def to_url(self, value):  
	return '%04d' % value  占四位，不够用0填满，超了则就按超了的位数来！
register_converter(FourDigitYearConverter, 'yyyy')  
			
urlpatterns = [  
		path('articles/2003/', views.special_case_2003),  
		path('articles/<yyyy:year>/', views.year_archive),  
		...  
	]  
```



## 前后端分离

前端一个人干(前端转成自定义对象)
	JSON.stringify()        json.dumps()
	JSON.parse()		json.loads()
后端另一个干(python后端用字典)
只要涉及到数据交互,一般情况下都是用的json格式
后端只负责产生接口,前端调用该接口能拿到一个大字典
后端只需要写一个接口文档 里面描述字典的详细信息以及参数的传递。

## 返回JSON对象

可以被序列化的对象都可以当作json返回。



```python
# 方法一：
def return_json(request):
    data = {'name': '我是papi', 'age': 18}
    res = json.dumps(data,ensure_ascii=False) # 不把内容进行转码
    return HttpResponse(res)

# 方法二：
def return_json(request):
    data = {'name': '我是papi', 'age': 18}
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

```

如果直接返回json的对象需要加

```python
return JsonResponse(l,safe=False)
```

request.get_full_path() 能够打印get请求过来的参数。
request.path 只能能够打印uri部分。

```python
/json/?id=123456
/json/
```

## 上传文件

```bash
# 前端实现
            <form action="" enctype="multipart/form-data">
              <div class="form-group">
                <input type="file" class="form-control">
              </div>
                {% csrf_token %}
              <button href="{% url 'add_book' %}" type="submit" class="btn btn-primary pull-right" formmethod="post" style="margin-top: 10px">保存</button>
            </form>
            
# 路由
path(r'up/',app01_views.upload_file,name='up'),

# 后端代码
def upload_file(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('uploadfile')
        print(file_obj.name) # 文件名
        with open(file_obj.name, 'wb') as f:
            for line in file_obj.chunks():
                f.write(line)
        return HttpResponse('收到了!')
    return render(request,'uploadfile.html')
```



request方法总结
	request.method
	request.GET
	request.POST
	request.FILES
	request.body  # 原生的二进制数据

RBAC (role based access control)
基于角色的权限管理

当你在做权限管理的时候 需要用到
在web领域权限就是一个个的url
简单判断用户是否有权限访问某个url思路
	获取用户想要访问的url
	与数据库中该用户可以访问的url进行对比



## [day54]()

djiango中配置文件的配置，

```bash
# 如果xxx不存在就会使用后者的配置
os.environ.setdefault('xxx','conf.settings')
```



## render原理

返回的还是标准的HttpResponse

```bash
from django.template import Template,Context
def re(request):
    temp = Template('<h1>{{ user }}</h1>')
    con = Context({"user":{"name":'jason',"password":'123'}})
    res = temp.render(con)
    print(res)
    return HttpResponse(res)
```





## FBV与CBV

视图函数并不只是指函数 也可以是类
	FBV(基于函数的视图) 面向函数式编程
	CBV(基于类的视图)   面向对象式编程
问题:基于CBV的视图函数 
get请求来就会走类里面get方法,post请求来就会走类里面post方法 为什么???

```python
urls.py中
	url(r'^login/',views.MyLogin.as_view())
views.py中
	from django.views import 
	class MyLogin(View):
		def get(self,request):
			print("from MyLogin get方法")
			return render(request,'login.html')
		def post(self,request):
			return HttpResponse("from MyLogin post方法")


研究方向 
	1.从url入手
    # 由于函数名加括号执行优先级最高,所以这一句话一写完会立刻执行as_view()方法
	url(r'^login/',views.MyLogin.as_view())  
	
	@classonlymethod
	def as_view(cls, **initkwargs):  # cls就是我们自己的写的类 MyLogin
		def view(request, *args, **kwargs):
			self = cls(**initkwargs)  # 实例化产生MyLogin的对象  self = MyLogin(**ininkwargs)
			if hasattr(self, 'get') and not hasattr(self, 'head'):
				self.head = self.get
			self.request = request
			self.args = args
			self.kwargs = kwargs
			# 上面的几句话都仅仅是在给对象新增属性
			return self.dispatch(request, *args, **kwargs)  # dispatch返回什么浏览器就会收到什么
			# 对象在查找属性或者方法的时候,你一定要默念:
            1.先从对象自己这里找
            2.然后从产生对象的类里面找
            3.最后类的父类依次往后
		return view
	
	通过源码发现url匹配关系可以变形成
	url(r'^login/',views.view)  # FBV和CBV在路由匹配上是一致的 都是url后面跟函数的内存地址
	2.当浏览器中输入login 会立刻触发view函数的运行
		def dispatch(self, request, *args, **kwargs):
		    # Try to dispatch to the right method; if a method doesn't exist,
		    # defer to the error handler. Also defer to the error handler if the
		    # request method isn't on the approved list.
		    # 我们先以GET为例
            # 判断当前请求方法是否在默认的八个方法内
		    if request.method.lower() in self.http_method_names:  
		    	# 反射获取我们自己写的类产生的对象的属性或者方法
		    	# 以GET为例  handler = getattr(self,'get','取不到报错的信息')
		    	# handler = get(request)
		    	handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
		    else:
		    	handler = self.http_method_not_allowed
		    return handler(request, *args, **kwargs)  # 直接调用我们自己的写类里面的get方法
		    # 源码中先通过判断请求方式是否符合默认的八个请求方法 然后通过反射获取到自定义类中的对应的方法执行
```

### CBV使用方法

```python
# urls.py
    path('login/', views.MyLogin.as_view(), name='login'),

# 视图中的函数定义
from django.views import View
class MyLogin(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self, request):
        print(request.POST.get('username'))
        return HttpResponse('成功')
```

## settings源码

1.django除了暴露给用户一个settings.py配置文件之外自己内部还有一个全局的配置文件。
2.我们在使用配置文件的时候可以直接直接导入暴露给用户的settings.py也可以使用django全局的配置文件并且后者居多。
	from django.conf import settings
3.django的启动入口是manage.py 

```python
import os
import s
if __name__ == "__main__":
	# django在启动的时候 就会往全局的大字典中设置一个键值对  值是暴露给用户的配置文件的路径字符串
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day54.settings")

class Settings(object):
	def __init__(self, settings_module):  # settings_module = 'day54.settings'
		# update this dict from global settings (but only for ALL_CAPS settings)
		for setting in dir(global_settings):  # django全局配置文件
			# dir获取django全局配置文件中所有的变量名
			if setting.isupper():  # 判断文件中的变量名是否是大写如果是大写才会执行/生效
                # 给settings对象设置键值对,settings[配置文件中大写的变量名] = 配置文件中大写的变量名所对应
				setattr(self, setting, getattr(global_settings, setting)) 
		# store the settings module in case someone later cares
        # day54.setting
		self.SETTINGS_MODULE = settings_module
        # mod = 模块settings(暴露给用户的配置文件)
		mod = importlib.import_module(self.SETTINGS_MODULE)  
		for setting in dir(mod):  # for循环获取暴露给用户的配置文件中所有的变量名
			if setting.isupper():  # 判断变量名是否是大写
				setting_value = getattr(mod, setting)  # 获取大写的变量名所对应的值
				setattr(self, setting, setting_value)  # 给settings对象设置键值对
				"""
				d = {}
				d['username'] = 'jason'
				d['username'] = 'egon'
				用户如果配置了就用用户的
				用户如果没有配置就用系统默认的
				其实本质就是利用字典的键存在就是替换的原理 实现了用户配置就用用户的用户没配置就用默认的
				"""
	
class LazySettings(LazyObject):
	    def _setup(self, name=None):
			# os.environ你可以把它看成是一个全局的大字典
			settings_module = os.environ.get(ENVIRONMENT_VARIABLE)  # 从大字典中取值键为                       # DJANGO_SETTINGS_MODULE所对应的值:day54.settings
			# settings_module = 'day54.settings'
			self._wrapped = Settings(settings_module)  # Settings('day54.settings')
			
settings = LazySettings()  # 单例模式	
```

## 模板层

打印执行的sql配置，在`settings.py`中的任意位置配置。

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```



### 模板传值

python的所有数据类型都可传到模板中，python中的函数也可以传到模板中，但是不支持传参数。

支持对象的方法，但是也不能传参数。

django在模板取值的时候统一使用.

```python
# 模板使用变量的两种方式
{{ }}
{% %}
```



```python
# 给模板传值的方式
# 方式1
    通过字典的键值对 指名道姓的一个个的传
    return render(request,'reg.html',{'n':n,'f':f})
# 方式2
    locals会将它所在的名称空间中的所有的名字全部传递给前端
    该方法虽然好用但是在某些情况下回造成资源的浪费
```

```python
# 模板呢
<body>
    <h3>{{ n }}</h3>
    <h3>{{ f }}</h3>
    <h3>{{ s }}</h3>
    <h3>{{ l }}</h3>
    <h3>{{ d }}</h3>
    <h3>{{ t }}</h3>
    <h3>{{ se }}</h3>
    <h3>{{ file_size }}</h3>
    <h3>{{ info }}</h3>
    <h3>{{ index }}</h3>
    <h3>{{ index }}</h3>
    <h3>{{ obj.get_self }}</h3>
    <h3>{{ obj.get_cls }}</h3>
    <h3>{{ obj.get_static }}</h3>
    <h3>{{ zzz }}</h3>
    <h3>{{ ctime }}</h3>
</body>

# views.py
def reg(request):
    # 先验证是否python所有的数据类型都可以被传递到前端
    n = 0
    # ss = ''
    f = 1.11
    s = '你妹的'
    l = [1,2,3,4,5,6,[12,3,4,{'name':'heiheihei'}]]
    d = {"name":'jason','password':123}
    t = (1,2,3,4,5)
    se = {1,2,3,4,5,6,7,}
    file_size = 12312312

    info = 'my name is jason and my age is 18'
    info1 = '傻大姐 撒旦 技术 大 萨达 了 奥斯卡 的健康两 三点卡是考虑到'
    def index(xxx):
        print(xxx)
        print('index')
        return '我是index函数的返回值'

    class Demo(object):
        def get_self(self):
            return '绑定给对象的方法'
        @classmethod
        def get_cls(cls):
            return '绑定给类的方法'
        @staticmethod
        def get_static():
            return '我是静态方法其实就是函数'
    obj = Demo()

    xxx = '<h1>波波棋牌室</h1>'
    yyy = '<script>alert(123)</script>'
    # 把html文本进行安全的返回
    from django.utils.safestring import mark_safe

    zzz = mark_safe('<h1>阿萨德搜啊第三款垃圾袋</h1>')

    from datetime import datetime
    ctime = datetime.now()

    return render(request,'index.html',locals())  # 为了教学方便 我们以后就用locals()
```

### 模板语法过滤器

在变量的后面使用,类似linux的管道符

```bash
{{ l | length }}


# 常用的标签
length         # 长度
default        # {{ n|default:"如果n为空就返回这里的结果" }} 必须规定为空时候返回的值
filesize       # 自动换算单位
truncatewords   #截断字符，按照空格截取，多余的就会显示...
                {{ info1 | truncatewords:3 }}
truncatechars   #按字符长度截取,空格算一个字符,三个点算一个字符
                {{ info | truncatechars:5 }}
safe            # 把python的html变量直接渲染
date            # 格式化时间
                {{ ctime | date:"FORMAT" }}
slice           # 切片
add             # 算数+
```

### 模板语法标签

逻辑相关

```python
# for循环取值
    {% for foo in l %}
        <p>{{ foo }}</p>
        {% empty %} 当for循环对象不能被for循环的时候会走empty逻辑
    {% endfor %}
    
# forloop每个循环对象的属性
    <br>
    {% for foo in l %}
    <p>{{ forloop }}</p>
    {% endfor %}
{'parentloop': {}, 'counter0': 0, 'counter': 1, 'revcounter': 7, 'revcounter0': 6, 'first': True, 'last': False}
{'parentloop': {}, 'counter0': 1, 'counter': 2, 'revcounter': 6, 'revcounter0': 5, 'first': False, 'last': False}
{'parentloop': {}, 'counter0': 2, 'counter': 3, 'revcounter': 5, 'revcounter0': 4, 'first': False, 'last': False}
{'parentloop': {}, 'counter0': 3, 'counter': 4, 'revcounter': 4, 'revcounter0': 3, 'first': False, 'last': False}
{'parentloop': {}, 'counter0': 4, 'counter': 5, 'revcounter': 3, 'revcounter0': 2, 'first': False, 'last': False}
{'parentloop': {}, 'counter0': 5, 'counter': 6, 'revcounter': 2, 'revcounter0': 1, 'first': False, 'last': False}
{'parentloop': {}, 'counter0': 6, 'counter0counter0': 7, 'revcounter': 1, 'revcounter0': 0, 'first': False, 'last': True}

counter0  索引
counter  循环次数
first    是否是第一个
last     是否是最后一个

#  条件判断,l是一个列表
{% for foo in l %}
    {% if forloop.first %}
        <p>这是第一次</p>
    {% elif forloop.last %}
        <p>这是最后一次</p>
        {% else %}
        <p>come on!!!</p>
    {% endif %}
{% endfor %}

这是第一次
come on!!!
come on!!!
come on!!!
come on!!!
come on!!!
这是最后一次


# 赋值别名，使用场景在嵌套的数据中，复杂的取值取一个别名，然后就可以重复使用别名
l = [1,2,3,4,5,6,[12,3,4,{'name':'heiheihei'}]]

    {% with l.6.3 as name %}
        {{ name }}
    {% endwith %}
    
# 取值结果
{'name':'heiheihei'}

# 字典的三个方法
keys
items
values
# 字典
d = {"name":'jason','password':123}

{% for key in d.keys %}
    {{ key }}
{% endfor %}

{% for value in d.values %}
    {{ value }}
{% endfor %}

{% for item in d.items %}
    {{ item }}
{% endfor %}

# 取值结果
name password
jason 123
('name', 'jason') ('password', 123)
```

### 自定义标签过滤器

自定义固定的三步走战略:
1.必须在你的应用下新建一个名为`templatetags`文件夹
2.在该文件夹内新建一个任意名称的py文件
3.在该py文件中固定先写下面两句代码

自定义过滤器只能有两个形参。但是可以把参数组合程其他数据类型然后再解开。

```python
from  django import template
register = template.Library()

# 自定义过滤器tag.py
@register.filter(name='baby')
def index(a,b):
	# 该过滤器只做一个加法运算是|add简易版本
	"""
	|length
	|add
	|default
	|filesizeformat
	|truncatewords
	|truncatechars
	|safe
	|slice

	:param a:
	:param b:
	:return:
	"""
	print('下午刚起床 一脸懵逼')
	return a + b

# 前端引用
    {% load tag %}
    {{ 12 | baby:10 }}
    
# 结果： 22
```

```python
# 自定义标签
# 支持传多个值
@register.simple_tag(name='jason')
def xxx(a,b,c,year):
	return '%s?%s|%s{%s'%(a,b,c,year)

# 前端传值
{% jason 11 22 33 year=2025 %}
```

```python
# 自定义inclusion_tag
"""
接收用户传入的参数然后作用于一个html页面
在该页面上渲染数据之后将渲染好的页面
放到用户调用inclusion_tag的地方
"""
# 写好的部分组件bigplus.html
<ul>
    {% for foo in l %}
        <li>{{ foo }}</li>
    {% endfor %}
</ul>



# 自定义inclusion_tag
# 这里需要传入一个模板
@register.inclusion_tag('bigplus.html')
def bigplus(n):
	l = []
	for i in range(n):
		l.append('第%s项'%i)
	return {'l':l}

# 在前端的任意页面引用
    {% load tag %}
    {% bigplus 5 %}
    
# 渲染的结果
 登录
第0项
第1项
第2项
第3项
第4项
```

### 模板的继承

当多个页面整体的样式都大差不差的情况下可以设置一个模板文件。
在该模板文件中使用block块划分多个分块。
之后子版在使用模板的时候可以通过block块的名字来选定到底需要修改哪一部分区域。

模板一般情况下 应该至少有三个可以被修改的区域
```django
{% block css %}
	子页面自己的css代码
{% endblock %}

{% block content %}
	子页面自己的html代码
{% endblock %}

{% block js %}
	子页面自己的js代码
{% endblock %}



# 模板的继承使用方式
{% extends 'home.html' %}

{% block css %}
	<style>
		h1 {
			color: red;
		}
	</style>
{% endblock %}

{% block content %}
<h1>登陆页面</h1>
	<form action="">
		<p>username:<input type="text" class="form-control"></p>
		<p>password:<input type="text" class="form-control"></p>
		<input type="submit" class="btn btn-danger">
	</form>
{% endblock %}

{% block js %}
...
{% endblock %}

# 一般情况下模板上的block越多页面的可扩展性就越强。
```

### 模板的导入

当你写了一个特别好看的form表单胡总和是列表标签，可以当作一个模板在哪里需要就在哪里导入。

```python
# 1.templates中定义漂亮的样式befaultful.html

# 2.在要引用的html文件中，引用
{% include 'befaultful.html' %}
```



作业：图书管理系统尝试使用模板的继承来写。

## 模型层

test.py中配置models查询数据库。

复制manager.py中的django配置文件。

```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day54.settings')

import django
django.setup()
```



### 单表查询必回13条

```python
# 1.查询表中所有对象
models.Book.objects.all()

# 增加数据
    # 方式1： create
    book_obj  = models.Book.objects.create(title='三国',price=19.99,create_time='2019-11-11')
    print(book_obj.title)
    
    # 方式2：对象点save()方法
    from datetime import datetime
    ctime = datetime.now()
    book_obj = models.Book(title='金瓶梅',price=96.66,create_time=ctime)
    book_obj.save()
    
# 2.条件查询
print(models.Book.objects.filter(id=1))
print(models.Book.objects.get(id=1))
print(models.Book.objects.get(pk=1))  # 会自动找到该表的主键作为查询条件，扩展性更好。


# 3.修改数据
models.Book.objects.filter(pk=1).update(price='88') # 修改价格为88
# 或者
book_obj = models.Book.objects.get(pk=2)
book_obj.price = 71 # 修改价格为71
book_obj.save()

# 4.删除对象
models.Book.objects.filter(pk=2).delete()

# 5.条件查询
# 它包含了与所给筛选条件相匹配的对象
print(models.Book.objects.filter(pk=1))

# 返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
print(models.Book.objects.get(pk=1))


# 6.反向查询
# 它包含了与所给筛选条件不匹配的所有对象
print(models.Book.objects.exclude(pk=1))

# 7.查询结果排序
print(models.Book.objects.order_by('price')) #默认升序
print(models.Book.objects.order_by('-price'))  # -就是降序

# 8.对结果反向排序，需要现有排序才行
print(models.Book.objects.order_by('price').reverse())

# 9.统计查询结果条数
print(models.Book.objects.filter(title='西游记').count())

# 10.查询返回结果的第一条和最后一条
print(models.Book.objects.all().first())
print(models.Book.objects.all().last())

# 11.判断是否有返回结果的布尔值
如果不存在数据返回结果是None布尔值本身也是false
print(models.Book.objects.filter(pk=1).exists())

# 12.查询特定字段
# 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
# model的实例化对象，而是一个可迭代的字典序列
# 得到的结果是列表套字典
print(models.Book.objects.values('title', 'price'))
<QuerySet [{'title': '红楼梦', 'price': Decimal('88.00')}, 
           {'title': '西游记', 'price': Decimal('54.00')}, 
           {'title': '水浒传', 'price': Decimal('89.00')}, 
           {'title': '三国演义', 'price': Decimal('42.00')}, 
           {'title': '西游记', 'price': Decimal('35.00')}]>


# 13. values_list(*field): 它与values()
print(models.Book.objects.values_list('title','price'))  # 得到的结果是列表套元组,不经常使用


# 非常相似，它返回的是一个元组序列，values返回的是一个字典序列
# 14.distinct(): 从返回结果中剔除重复纪录
    """
    去重的前提是 一定要有完全重复的数据 才能去重
    """
print(models.Book.objects.filter(title='三国演义').distinct())
print(models.Book.objects.values('title','price','create_time').distinct())
```

## 双下划线查询

```python
# 查询价格大于50的书籍
res = models.Book.objects.filter(price__gt = 50)

# 查询价格小于50的书籍
res = models.Book.objects.filter(price__lt = 50)

# 查询的大于等于或者小于等于
res = models.Book.objects.filter(price__lte = 42)
res1 = models.Book.objects.filter(price__gte = 42)

# 查询加个是88或者35或者42的书籍
res = models.Book.objects.filter(price__in=[88,35,42])

# 查询价格在50到100之间的书籍,开头结尾都包含
res = models.Book.objects.filter(price__range=(50,100))

# 模糊查询,数据名称包含'记'的。
# 如果是英文结尾的可以使用title__icontains可以忽略大小写。
res = models.Book.objects.filter(title__contains='记')

# 查询书籍名称是以3开头的
res = models.Book.objects.filter(title__startswith='红')
# 什么结尾
res1 = models.Book.objects.filter(title__endswith='记')

# 查询出版日期是2021年的
res = models.Book.objects.filter(create_time__year=2024)
```

### 跨表查询

#### 一对多的增删改查

1.一对多字段增加数据，有两种方法一种是直接给外键字段赋值外键的id，或者先把外键对象查出来赋值外键对象。

增加一本书籍，指定出版社。

```python
# 方法一:
# models.Book.objects.create(title='钢铁是怎样练成的',price='50.32',publish_date='2025-05-04',publish_id=5)


# 方法二:
# 先把出版社对象查出来
publish_obj = models.Publish.objects.filter(id=1).first()
# 然后再复制
models.Book.objects.create(title='三国演义',price='154',publish_date='2015-07-01',publish=publish_obj)
```

2.修改书籍的出版社

```bash
# 方法一：
models.Book.objects.filter(title='Java核心技术').update(publish_id = 3)

# 方法二：
publish_obj = models.Publish.objects.filter(id=2).first()
models.Book.objects.filter(title='Java核心技术').update(publish=publish_obj)
```

3.删除出版社，对应的书籍也会被删除`on_delete=models.CASCADE`。

```python
# 删除出版社
models.Publish.objects.filter(pk=1).delete()
```



#### 多对多字段的增删改查

4.给书籍添加出版社

`add()`是给书籍添加作者括号内既可以传数字也可以传对象并且支持一次性传多个逗号隔开即可.

```python
# 给书籍钢铁是怎样练成的添加两个作者
book_obj = models.Book.objects.filter(title='钢铁是怎样练成的').first() # type: models.Book
book_obj.authors.add(9,10) # 直接使用作者表的主键id

# 另一种方式
author1 = models.Author.objects.filter(id=5).first()
author2 = models.Author.objects.filter(id=6).first()
book_obj = models.Book.objects.filter(pk=14).first() # type: models.Book
book_obj.authors.add(author1,author2)
```

改

```python
# 把《java编程思想》的作者修改为2,5
book_obj = models.Book.objects.filter(title='Java编程思想').first() # type: models.Book
author1 = models.Author.objects.filter(pk=2).first()
author2 = models.Author.objects.filter(pk=5).first()
book_obj.authors.set([author1, author2])
```
`set()`括号内需要传一个可迭代对象可迭代对象中可以是多个数字组合也可以是多个对象组合但是不要混着用。

给书籍删除作者对象

`remove()`括号内既可以传数字也可以传对象并且支持传对个逗号隔开即可。

```python
book_obj = models.Book.objects.filter(title='计算机图形学').first() # type: models.Book
book_obj.authors.remove(10)  # 删除id是10的作者id

# 方法二:
author1 = models.Author.objects.filter(pk=1).first()
author2 = models.Author.objects.filter(pk=2).first()
book_obj.authors.remove(author1,author2)
```

将某本书和作者的关系全部清空

```python
book_obj = models.Book.objects.filter(pk=5).first()
book_obj.authors.clear()
```

#### 正向查询与反向查询

正向与反向的概念

一对一
正向：author---关联字段在author表里--->authordetail		按字段
反向：authordetail---关联字段在author表里--->author		按表名小写

一对多
正向：book---关联字段在book表里--->publish		按字段
反向：publish---关联字段在book表里--->book		按表名小写_set.all() 因为一个出版社对应着多个图书

多对多
正向：book---关联字段在book表里--->author		按字段
反向：author---关联字段在book表里--->book		按表名小写_set.all() 因为一个作者对应着多个图书

正向查询按外键字段
反向查询按表名小写

基于对象的跨表查询(子查询:将一张表的查询结果当做另外一个查询语句的条件)

强调: 在书写orm语句的时候跟写sql语句一样不要尝试着一次性写完应该做到写一点看一点再一点。

当反向查询的结果是多个的时候需要使用`表小写_set`。

```python
# 查询书籍深度学习的出版社名称
book_obj = models.Book.objects.filter(title='深度学习').first() # type: models.Book
print(book_obj.publish.name)

# 查询书籍深度学习的作者
book_obj = models.Book.objects.filter(title='深度学习').first() # type: models.Book
authors, = book_obj.authors.all()
print(authors.name)

# 查询作者王五的家庭地址
author = models.Author.objects.filter(name='王五').first() # type: models.Author
print(author.author_detail.addr)

# 查询北京大学出版社的出版的书籍
publish_obj = models.Publish.objects.filter(name='北京大学出版社').first() # type: models.Publish
books = publish_obj.book_set.all()
for book in books:
    print(book.title)

# 查询作者是jason写过的所有书籍pk是作者id
author_obj = models.Author.objects.filter(pk=3).first() # type: models.Author
books = author_obj.book_set.all()
for book in books:
    print(book.title)

# 查询电话号码13000130010的作者
detail = models.AuthorDetail.objects.filter(phone=13000130010).first() # type: models.AuthorDetail
print(detail.author.name)


# 查询书籍《数据库系统概念》的作者的电话号码
book_obj = models.Book.objects.filter(title='数据库系统概念').first() # type: models.Book
for auther in book_obj.authors.all(): # 这里返回的是一个列表所以要循环一下
    print(auther.author_detail.phone)
```

#### 联合查询

基于双下划綫的跨表查询(连表操作)

- left join
- inner join
- right join
- union

```python
# 查询钱七的手机号
res = models.Author.objects.filter(name='钱七').values('author_detail__phone','author_detail__addr')
print(res.first())

## 反向查询
res1 = models.AuthorDetail.objects.filter(author__name='钱七').values('author__age')
print(res1)

# 查询作者张三的年龄和手机号
res = models.Author.objects.filter(name='张三').values('age', 'author_detail__phone')
print(res)
## 反向查询
res = models.AuthorDetail.objects.filter(author__name='张三').values('author__age', 'phone')
print(res)

# 查询手机号码是13200132008的作者年龄和姓名
## 正向
res = models.Author.objects.filter(author_detail__phone=13200132008).values('name', 'age')
print(res)

## 反向
res = models.AuthorDetail.objects.filter(phone=13200132008).values('author__name', 'author__age')
print(res)

# 查询书籍id是1 的作者的电话号码
# 只要表里面有外键字段 你就可以无限制跨多张表
res = models.Book.objects.filter(pk=7).values('authors__author_detail__phone')
# res1 = models.Book.objects.filter(pk=1).values('外键字段1__外键字段2__外键字段3__普通字段')
print(res)

# 查询出版社为清华大学出版社的所有图书的名字和价格
res = models.Publish.objects.filter(name='清华大学出版社').values('book__title','book__price')
print(res)

# 2.查询北方出版社出版的价格大于19的书
res = models.Book.objects.filter(price__gt=19,publish__name='北方出版社').values('title','publish__name')
print(res)
```



#### 聚合查询

```python
# 聚合查询
from django.db.models import Max,Min,Count,Avg,Sum

res1 = models.Book.objects.aggregate(Max('price'))
res2 = models.Book.objects.aggregate(Min('price'))
res3 = models.Book.objects.aggregate(Count('title'))
res4 = models.Book.objects.aggregate(Avg('price'))
res5 = models.Book.objects.aggregate(Sum('price'))
print(res1,res2,res3,res4,res5)
```

#### 分组查询

```python
from django.db.models import Max, Min, Count, Avg, Sum

# 统计每本书的作者个数
res = models.Book.objects.annotate(author_num = Count('authors')).values('author_num', 'title')
print(res)

# 统计每个出版社价格最便宜的书
res = models.Publish.objects.annotate(mmp = Min('book__price')).values('name','mmp')
print(res)

# 统计作者不止一个的图书
"""
只要是queryset对象
就可以无限制的调用queryset对象的方法!!!
最最常用的就是对一个已经filter过滤完的数据
再进行更细化的筛选
"""
res = models.Book.objects.annotate(author_num = Count('authors')).filter(author_num__gt=1)
print(res)

# 查询各个作者出的书的总价格
res = models.Author.objects.annotate(sp=Sum('book__price')).values('name','sp')
print(res)
```

#### 查询与Q查询

```python
from django.db.models import F

"""
F查询的本质就是从数据库中获取某个字段的值,查询库存数大于卖出数的书籍。
之前查询等号后面的条件都是我们认为输入的,现在变成了需要从数据库中获取数据放在等号后面。
"""
res = models.Book.objects.filter(kucun__gt=F('maichu'))

# 将库存的数量加1000
models.Book.objects.update(kucun=F('kucun')+1000)

from django.db.models.functions import Concat
from django.db.models import Value
# 把指定的书后面加上新款
models.Book.objects.filter(pk=5).update(title=Concat(F('title'),Value('-新款')))

# Q查询
# 查询书籍名称是三国演义或者价格是444.44
from django.db.models import Q

res = models.Book.objects.filter(title='三国演义',price=444.44)  # filter只支持and关系
res1 = models.Book.objects.filter(Q(title='深度学习'),Q(price=130))  # 如果用逗号那么还是and关系
res2 = models.Book.objects.filter(Q(title='深度学习')|Q(price=79))  # | 是或者的意思
res3 = models.Book.objects.filter(~Q(title='三国演义')|Q(price=79))  # ~表示取反

# Q高级用法
q = Q()
q.connector = 'or'  # 修改查询条件的关系默认是and
q.children.append(('title__contains','深度学习'))  # 往列表中添加筛选条件
q.children.append(('price__gt',79))  # 往列表中添加筛选条件
res = models.Book.objects.filter(q)  # filter支持你直接传q对象但是默认还是and关系
print(res)
```

### 查询优化

```python
defer与only
res = models.Author.objects.all().values('name')  
# 这样虽然能拿到对象的name属性值，但是已经是queryset里面套字典的格式，我现在想拿到queryset里面放的还是一个个的对象，并且这这些对象“只有”name属性，其他属性也能拿，但是会重新查询数据库，类似于for循环N次走N次数据库查询
res = models.Author.objects.all().only('name')  # 一旦指导了only就不要取对象没有的属性值了，如果指定了就会循环的去查找数据库。

res = models.Author.objects.all().defer('title')

defer与only刚好相反，取不包括括号内的其他属性值


# select_related和prefetch_related
# 如果使用的是all()字段会通过sql联表，直接连表操作select_related里面只能放外键字段而且只能放一对一和一对多的字段，代码会把外键的字段整合成一个表再进行查询，效率会更高。
# 如果外键表中还有外键可以使用models.Book.objects.all().select_related('外键1__外键2__外键3')
res = models.Book.objects.all().select_related('publish')

# prefetch_related 不主动联表
res = models.Book.objects.all().prefetch_related('publish')

# 先把表的结果查出来，然后讲几个表查询的结果来进行处理，省去了联表的时间。
```



### 数据库事务

```python
from django.db import transaction

with transaction.atomic():
    """数据库操作
    比如添加书籍和添加作者要同时进行且数据要保证AICD就使用事务
    在该代码块中书写的操作同属于一个事务
    """
print('出了代码块事务就结束')
```

## AJAX

它可以异步地向服务器发送请求，在等待响应的过程中，不会阻塞当前页面，在这种情况下，浏览器可以做自己的事情。直到成功获取响应后，浏览器才开始处理响应数据。

### 计算器实例

在不刷新网页的情况下点击计算，通过ajax发送请求到服务端，并填充在相应的格子中。

![image-20250603174032559](images\image-20250603174032559.png)

```html
<body>
<input type="text" id="i1">+<input type="text"id="i2">=<input type="text" id="i3">
<button id="b1" class="btn">求和</button>

<script>
        // 给按钮绑定事件
        $('#b1').on('click',function () {
        alert(123)
        // 点击按钮朝后端发送post请求
        $.ajax({
            url:'',  // 控制发送给谁 不写就是朝当前地址提交
            type:'post',  // 发送方式是post请求
            data:{'i1':$('#i1').val(),'i2':$('#i2').val()},  // 发送的数据
            success:function (data) {  // data形参用来接收异步提交的结果
                alert(data)
                // 将后端计算好的结果 通过DOM操作 渲染到第三个input矿中
                $('#i3').val(data)
            }
        })
        })
</script>
</body>
```

后端代码

```python
def index(request):
    if request.is_ajax():
        if request.method == 'POST':
            v1 = request.POST.get('i1')
            v2 = request.POST.get('i2')
            v3 = int(v1) + int(v2)

            return HttpResponse(v3)
    return render(request,'index.html')
```

contentType前后端传输数据编码格式，前后端传输数据编码格式。

1. urlencoded
2. formdata
3. json

### form表单
默认使用的编码格式是urlencoded，数据格式:name=jason&pwd=123，django后端针对urlencoded编码格式的数据会自动解析并放到request.POST中供用户获取。

可以修改为formdata传文件django后端针对只要是符合urlencoded编码格式的数据(name=jason&pwd=123)都会自动解析并放到request.POST中供用户获取如果是文件只要你指定的编码是formdata就会自动解析并放到request.FILES中。

总结:前后端传输数据的时候一定要保证数据格式和你的编码格式是一致的不能骗人家!!!

```python
# 不能够识别文件，只能把文件名通过kv的方式传递后后端
<form action="" method="post" enctype="application/x-www-form-urlencoded">
    <p>username: <input type="text" name="name"></p>
    <p>password: <input type="password" name="password"></p>
    <p><input type="file" name="myfile"></p>
    <p><input type="submit"></p>
</form>


# 后端可以使用request.FILES解析到文件，正常的input值，后端可以直接收到
<form action="" method="post" enctype="multipart/form-data">
    <p>username: <input type="text" name="name"></p>
    <p>password: <input type="password" name="password"></p>
    <p><input type="file" name="myfile"></p>
    <p><input type="submit"></p>
</form>
```

### ajax提交数据

ajax默认数据提交方式也是urlencoded

ajax发送json格式数据，django后端针对json格式的数据并不会自动解析放到`request.POST`或者`request.FILES`里面它并不会解析json格式数据而是将它原封不动的放在`request.body`中。

使用jquery类型的ajax提交POST请求。

```python
<button class="btn btn-primary" id="b1">发送ajax post</button>

<script>
      $('#b1').on('click',function () {
          alert(123)
          // 点击按钮 朝后端发送post请求
          $.ajax({
              url:'',  // 控制发送给谁 不写就是朝当前地址提交
              type:'post',  // 发送方式是post请求
              data:JSON.stringify({'username':'jason','password':123}),  // 发送的数据
              contentType:'application/json',  // 告诉后端你这次的数据是json格式
              success:function (data) {  // data形参用来接收异步提交的结果
                  alert(data)
                  // 将后端计算好的结果 通过DOM操作 渲染到第三个input矿中
                  $('#i3').val(data)
              }
          })
      })
    
# 后端接收到的信息
def test(request):
    print(request.body)
    print(request.content_type)

# ->    
b'{"username":"jason","password":123}'
application/json
```

### ajax传输文件

和form表单差不多，在设置了传输的类型是`fromData`之后，后端可以接收到request.POST的信息和request.FILES的文件信息。

![](images\image-20250605-1.png)

```python
<form action="">
    <p><input type="file" name="myfile" id="d1"></p>
    <button type="button" class="" id="b1">发送文件</button>
</form>

<p>MESSAGE: <input type="text" id="i3"></p>

<script>
$('#b1').on('click',function () {
	// ajax传输文件 建议使用内置对象formdata
	var formData = new FormData();  // 既可以传普通的键值对也可以传文件
	// 添加普通键值
	formData.append('username','jason');
	formData.append('password','123');
	// 传文件
	// 如何获取文件标签所存储的文件对象?  固定语法
	// 1.先用jQery查找到存储文件的input标签
	// 2.将jQuery对象转成原生js对象
	// 3.利用原生js对象的方法 .files[0]获取到标签内部存储的文件对象
	// 4.一定要指定两个参数都为false
	formData.append('my_file',$('#d1')[0].files[0]);
	$.ajax({
		url:'',  // 控制发送给谁 不写就是朝当前地址提交
		type: 'post',  // 发送方式是post请求
		data: formData, // 发送的数据

		// ajax发送文件需要指定两个额外的参数
		processData:false,  // 告诉前端不要处理数据
		contentType:false,  // 不适用任何编码  因为formdata对象自身自带编码 django后端也能够识别formdata对象

		success:function (data) {  // data形参用来接收异步提交的结果
			alert(data)
			// 将后端计算好的结果 通过DOM操作 渲染到第三个input矿中
			$('#i3').val(data)
		}
	})
})
</script>

# 后端接收到的数据
def form(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            return HttpResponse('收到了')
    return render(request, 'form.html')
# ---res---
<QueryDict: {'username': ['jason'], 'password': ['123']}>
<MultiValueDict: {'my_file': [<InMemoryUploadedFile: 2.png (image/png)>]}>
```

### django序列化组件serializers

```python
from django.core import serializers

def listbook(request):
    books = models.Book.objects.all()
    res = serializers.serialize('json', books)
    return render(request, 'listbook.html', locals())
```

删除提示的组件，每个版本的实际写法不一致。

```html
<script>
// 绑定按钮
$('.btn-del').click(function (){
Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
}).then((result) => {
  if (result.value) {
    // 显示加载状态
    Swal.fire({
      title: 'Processing...',
      html: 'Deleting your file...',
      allowOutsideClick: false,
      showConfirmButton: false,
      willOpen: () => {
        Swal.showLoading();
      }
    });

    // 获取要删除的 ID（假设你有一个变量存储 ID）
    var $btnEle = $(this); // 替换为你的实际 ID 获取方式
    var bookId = $btnEle.attr('book_id');

    // 发送 POST 请求到删除 API
    $.ajax({
      url: '', // 替换为你的实际 API 地址
      type: 'POST',
      data: {
        id: bookId,
      },
      // dataType: 'json',
      success: function(response) {
        // 请求成功处理
        Swal.fire(
          'Deleted!',
          'Your file has been deleted.',
          'success'
        ).then(() => {
          // 刷新页面或移除被删除的元素
          // 例如：$('#item-' + itemId).remove();
            $btnEle.parent().parent().remove();
        });
      },
      error: function(xhr, status, error) {
        // 请求失败处理
        Swal.fire(
          'Error',
          'Failed to delete: ' + xhr.responseText,
          'error'
        );
      }
    });
  }
})
    });
</script>
```

## 自定义分页器

主要的的思路就是从前端获取到page_num,后端控制orm查询从page_num到第几页，生成相应的翻页标签之后再到前端进行渲染。

django也有自带的分页器。

```python
class Pagination(object):
    def __init__(self, current_page, all_count, per_page_num=2, pager_count=11):
        """
        封装分页相关数据
        :param current_page: 当前页
        :param all_count:    数据库中的数据总条数
        :param per_page_num: 每页显示的数据条数
        :param pager_count:  最多显示的页码个数

        用法:
        queryset = model.objects.all()
        page_obj = Pagination(current_page,all_count)
        page_data = queryset[page_obj.start:page_obj.end]
        获取数据用page_data而不再使用原始的queryset
        获取前端分页样式用page_obj.page_html
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1

        if current_page < 1:
            current_page = 1

        self.current_page = current_page

        self.all_count = all_count
        self.per_page_num = per_page_num

        # 总页码
        all_pager, tmp = divmod(all_count, per_page_num)
        if tmp:
            all_pager += 1
        self.all_pager = all_pager

        self.pager_count = pager_count
        self.pager_count_half = int((pager_count - 1) / 2)

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page_num

    @property
    def end(self):
        return self.current_page * self.per_page_num

    def page_html(self):
        # 如果总页码 < 11个：
        if self.all_pager <= self.pager_count:
            pager_start = 1
            pager_end = self.all_pager + 1
        # 总页码  > 11
        else:
            # 当前页如果<=页面上最多显示11/2个页码
            if self.current_page <= self.pager_count_half:
                pager_start = 1
                pager_end = self.pager_count + 1

            # 当前页大于5
            else:
                # 页码翻到最后
                if (self.current_page + self.pager_count_half) > self.all_pager:
                    pager_end = self.all_pager + 1
                    pager_start = self.all_pager - self.pager_count + 1
                else:
                    pager_start = self.current_page - self.pager_count_half
                    pager_end = self.current_page + self.pager_count_half + 1

        page_html_list = []
        # 添加前面的nav和ul标签
        page_html_list.append('''
                    <nav aria-label='Page navigation>'
                    <ul class='pagination'>
                ''')
        first_page = '<li><a href="?page=%s">首页</a></li>' % (1)
        page_html_list.append(first_page)

        if self.current_page <= 1:
            prev_page = '<li class="disabled"><a href="#">上一页</a></li>'
        else:
            prev_page = '<li><a href="?page=%s">上一页</a></li>' % (self.current_page - 1,)

        page_html_list.append(prev_page)

        for i in range(pager_start, pager_end):
            if i == self.current_page:
                temp = '<li class="active"><a href="?page=%s">%s</a></li>' % (i, i,)
            else:
                temp = '<li><a href="?page=%s">%s</a></li>' % (i, i,)
            page_html_list.append(temp)

        if self.current_page >= self.all_pager:
            next_page = '<li class="disabled"><a href="#">下一页</a></li>'
        else:
            next_page = '<li><a href="?page=%s">下一页</a></li>' % (self.current_page + 1,)
        page_html_list.append(next_page)

        last_page = '<li><a href="?page=%s">尾页</a></li>' % (self.all_pager,)
        page_html_list.append(last_page)
        # 尾部添加标签
        page_html_list.append('''
                                           </nav>
                                           </ul>
                                       ''')
        return ''.join(page_html_list)
    
    
# views中使用
def listbook(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 100, 'msg': ''}
            book_id = request.POST.get('id')
            models.Book.objects.filter(pk=book_id).delete()
            back_dic['msg'] = '真的删除了!'

            return JsonResponse(back_dic)
    books = models.Book.objects.all()
    all_count = books.count()
    # 当前页
    current_page = request.GET.get('page',1)

    pagenaebar = Pagination(current_page,all_count,per_page_num=10, pager_count=9)
    # all_count        所有的数据量
    # per_page_num=10  每页显示多少条
    # pager_count=9    一页显示多少页码
    
    # 查询本页开头到结尾的数据
    page_data = books[pagenaebar.start:pagenaebar.end]
    page_html = pagenaebar.page_html()
    
# 模板
{{ page_html | safe }}
```

## django自带分页器

```python
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.objects.all()  # 获取所有文章
    paginator = Paginator(articles, 10)  # 每页显示10条
    page_number = request.GET.get('page')  # 获取当前页码
    page_obj = paginator.get_page(page_number)  # 获取分页对象
    return render(request, 'article_list.html', {'page_obj': page_obj})

# 在模板中渲染
<div class="pagination">
    <span class="step-links">
        {% if page_obj.has_previous %}
            <a href="?page=1">&laquo; 第一页</a>
            <a href="?page={{ page_obj.previous_page_number }}">上一页</a>
        {% endif %}
        
        <span class="current">
            第 {{ page_obj.number }} 页，共 {{ page_obj.paginator.num_pages }} 页。
        </span>
        
        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">下一页</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">最后一页 &raquo;</a>
        {% endif %}
    </span>
</div>

# 这个变量是列表中展示的对象是后端返回的list
{{ page_obj.object_list }}
```



## FORMS组件

需求：

1. 自己手动实现一个注册功能。
2. 当用户的用户名包含金瓶梅，提示不符合社会主义核心价值观。
3. 当用户的密码短于3位，提示密码太短了 不符合要求。

django返回页面的流程。

1.前端页面搭建——渲染页面。
2.将数据传输到后端做校验——校验数据。
3.展示错误信息——展示信息。

forms组件能够直接帮你完成上面的三步操作。

手动的方式把报错信息渲染到前端。

```python
def login(request):
    error_msg = {'username':'', 'password':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        if '金瓶梅' in username:
            error_msg['username'] = '不能含有金瓶梅'
        password = request.POST.get('password')
        if len(password) < 3:
            error_msg['password'] = '密码不能小于3位'

    return render(request, 'login.html',{'error_msg': error_msg})

# 前端渲染
<form action="" method="post" enctype="application/x-www-form-urlencoded">
    <h2 class="h2">注册</h2>
    <p>username: <input type="text" name="username"></p>
    <span  style="color: red">{{ error_msg.username }}</span>
    <p>password: <input type="password" name="password"></p>
    <span  style="color: red">{{ error_msg.password }}</span>
    <input type="submit">
</form>
```



### 1.forms组件基本用法

校验用户提交的字段格式。

```python
class LoginForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=3)  # 用户名最长八位最短三位
    password = forms.CharField(max_length=8, min_length=5)  # 密码最长八位最短五位
    email = forms.EmailField()  # email必须是邮箱格式

# 1.基本使用
# 把需要校验的数据以字典的方式传递给自定义的类实例化产生对象
form_obj = LoginForm({'username': 'admin', 'password':'1345','email':'xx@x.com'})

# 查看传入的数据是否合法
print(form_obj.is_valid())

# 查看错误的数据
print(form_obj.errors)

# 查看通过检验的数据
print(form_obj.cleaned_data)
```

注意事项:

- 自定义类中所有的字段默认都是必须要传值的，不能少传。
- 可以额外传入类中没有定义的字段名forms组件不会去校验也就意味着多传一点关系没有。

### 2.forms渲染页面的三种方式

后端实现

```python
class LoginForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=3)  # 用户名最长八位最短三位
    password = forms.CharField(max_length=8, min_length=5)  # 密码最长八位最短五位
    email = forms.EmailField()  # email必须是邮箱格式

def lg(request):
    form_obj = LoginForm()
    if request.method == 'POST':
        form_obj = LoginForm(request.POST)
        # 如果数据都是合法的那么在写入数据库或者验证之后就可以返回正常的页面了
        if form_obj.is_valid():
            return HttpResponse('ok')
    # 但是上面的不合法就会被渲染错误信息之后返回
    return render(request, 'lg.html', {'form_obj': form_obj})
```



```html
<p>第一种渲染页面的方式(封装程度太高一般只用于本地测试通常不适用)</p>
{{ form_obj.as_p }}  
{{ form_obj.as_ul }}
{{ form_obj.as_table }}

<p>第二种渲染页面的方式(可扩展性较高 书写麻烦)</p>
<p>{{ form_obj.username.label }}{{ form_obj.username }}</p>
<p>{{ form_obj.password.label }}{{ form_obj.password }}</p>
<p>{{ form_obj.email.label }}{{ form_obj.email }}</p>

<p>第三种渲染页面的方式(推荐)</p>
{% for foo in form_obj %}
	<p>{{ foo.label }}{{ foo }}</p>
{% endfor %}
```

注意事项
1.forms组件在帮你渲染页面的时候只会渲染获取用户输入的标签提交按钮需要你手动添加.
2.input框的label注释不指定的情况下默认用的类中字段的首字母大写.

校验数据的时候可以前后端都校验做一个双重的校验,但是前端的校验可有可无,而后端的校验则必须要有,因为前端的校验可以通过爬虫直接避开。

前端取消浏览器校验功能，form标签指定novalidate属性即可。
```html
<form action="" method='post' novalidate></form>
```

### 3.展示错误信息

```python
class LoginForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=3,label='用户名')  # 用户名最长八位最短三位
    password = forms.CharField(max_length=8, min_length=5, label='密码')  # 密码最长八位最短五位
    email = forms.EmailField()  # email必须是邮箱格式

def lg(request):
    form_obj = LoginForm()
    if request.method == 'POST':
        # 如果数据都是合法的那么在写入数据库或者验证之后就可以返回正常的页面了
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('ok')
    # 但是上面的不合法就会被渲染错误信息之后返回
    return render(request, 'lg.html', {'form_obj': form_obj})

# 前端渲染
<form action="" method="post" enctype="application/x-www-form-urlencoded" novalidate>
    {% for foo in form_obj %}
        <p>{{ foo.label }}:{{ foo }}
        <p style="color: red">{{ foo.errors.0 }}</p>
        </p>
    {% endfor %}
    <input type="submit">
</form>
```

### 4.钩子函数

forms组件暴露给用户 可以自定义的校验规则

- 全局钩子 

- 局部钩子

用法:在自定义的form类中书写方法即可

```python
class LoginForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=3,label='用户名')  # 用户名最长八位最短三位
    password = forms.CharField(max_length=8, min_length=5, label='密码')  # 密码最长八位最短五位
    confirm_password = forms.CharField(max_length=8, min_length=5, label='确认密码')  # 确认密码最长八位最短五位
    email = forms.EmailField()  # email必须是邮箱格式

    # 局部钩子函数用来验证用户名中的特俗字符
    def clean_username(self):
        # 钩子函数，验证用户名是否合法
        username = self.cleaned_data.get('username')
        if '666' in username:
            self.add_error('username', '用户名不能包含666')
        return username

    # 全局钩子函数用来验证密码是否一致
    def clean(self):
        # 钩子函数，验证密码是否一致
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data
    
# 后端代码
def lg(request):
    form_obj = LoginForm()
    if request.method == 'POST':
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('ok')
    return render(request, 'lg.html', {'form_obj': form_obj})

# 前端渲染
<form action="" method="post" enctype="application/x-www-form-urlencoded" novalidate>
    {% for foo in form_obj %}
        <p>{{ foo.label }}:{{ foo }}
        <p style="color: red">{{ foo.errors.0 }}</p>
        </p>
    {% endfor %}
    <input type="submit">
</form>
```

![](D:\LearnDjango\images\QQ截图20250611100308.png)

## 5.forms中的其它字段和参数

```python
class LoginForm(forms.Form):

    username = forms.CharField(max_length=8,min_length=3,initial='username',label='用户名',error_messages={
        'max_length': '用户名不能超过8位',
        'min_length': '用户名不能小于3位',
       'required': '用户名不能为空'
    },widget=forms.TextInput(attrs={'class': 'form-control haha'}))

    password = forms.CharField(max_length=8,min_length=3,label='密码',error_messages={
       'max_length': '密码不能超过8位',
       'min_length': '密码不能小于3位',
       'required': '密码不能为空'
    },widget=forms.PasswordInput(attrs={'class': 'form-control haha'}))

    confirm_password = forms.CharField(max_length=8,min_length=3,label='确认密码',error_messages={
      'max_length': '密码不能超过8位',
      'min_length': '密码不能小于3位',
      'required': '密码不能为空'
    },widget=forms.PasswordInput(attrs={'class': 'form-control haha'}),required=False,validators=[RegexValidator(r'^[0-9]+$', '请输入数字'),
                                   RegexValidator(r'^159[0-9]+$', '数字必须以159开头')])

    # email格式校验
    email = forms.EmailField(label='邮箱',error_messages={
      'required': '邮箱不能为空',
      'invalid': '邮箱格式不正确'
    })
    
# -------------><-------------
required          是否必填
label 		      注释信息
error_messages    报错信息
initial		      默认值
widget		      控制标签属性和样式
widget=widgets.PasswordInput()   # type="password"
				  控制标签属性
widget=widgets.PasswordInput(attrs={'class':'form-control c1 c2','username':'jason'})
validators        自定义校验规则
```

### form表单中的其它选项

```python
     # 单选的radio框
    gendenr = forms.ChoiceField(choices=[(1, '男'), (2, '女'), (3, '保密')], label='性别', initial=3,widget=forms.RadioSelect)

    # 单选select框
    hobby = forms.ChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好', initial=3,widget=forms.Select)

    # 多选的select框
    hobby1 = forms.MultipleChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好1', initial=[1, 3],widget=forms.SelectMultiple)

    # 单选的checkbox框
    hobby2 = forms.ChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好2', initial=3,widget=forms.CheckboxInput(attrs={'class': 'form-control haha'}))

    # 多选的checkbox框
    hobby3 = forms.MultipleChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好3', initial=[1, 3],widget=forms.CheckboxSelectMultiple)
```



## 操作Cookie

cookie只保存在客户端，服务端生成并配置，用来记录客户端的状态，发送给浏览器缓存。明文传输最大只能保存4k的数据。默认有效期是14天。

```python
def login(request):
    error_msg = {'username':'', 'password':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'alex' and password == '123':
            # 先获取url中跳转的参数
            next_url = request.GET.get('next')
            # 如果有就直接跳转到要访问的页面
            if next_url:
                return redirect(next_url)
        else:
            # 如果没有跳转的参数则直接跳转到首页
            obj = redirect('/home/')
        # cookie的过期时间，单位是秒，3600代表一个小时
        obj.set_cookie('username', username, max_age=3600)
        return obj
    # get请求直接返回登陆页
    return render(request, 'login.html',{'error_msg': error_msg})


from functools import wraps

def login_auth(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        # 从request中获取cookie
        # print(request.path)
        # print(request.get_full_path())
        target_url = request.get_full_path()
        if request.COOKIES.get('username'):
            res = func(request,*args,**kwargs)
            return res
        else:
            return redirect('/login/?next=%s'%target_url)
    return inner

@login_auth
def home(request):
    username = request.COOKIES.get('username')
    return render(request, 'home.html',{'username': username})

def loginout(request):
    obj = redirect('/login/')
    obj.delete_cookie('username')
    return obj
```



## 操作session

session服务器会保存一份在django_session表中。

```python
def set_session(request):
    request.session['username'] = 'alex'
    request.session['age'] = 18
    request.session['ts'] = int(time.time())
    # 设置seession的超时时间是3600s
    # set_expiry(value)有几种情况
    # 1 如果value是一个整数，session将在这些秒数后到期。
    # 2 如果value是一个datatime或timedelta，session将在这个时间后到期。
    # 3 如果value是0,用户会话的Cookie将在用户的浏览器关闭时过期。
    # 4 如果value是None, session会使用全局session失效策略。
    # 5 设置小于0的整数，session将在会话的Cookie到期时过期。
    request.session.set_expiry(3600)
    return HttpResponse('设置session')

def get_session(request):
    username = request.session.get('username')
    age = request.session.get('age')
    ts = request.session.get('ts')

    print(username,age,ts)
    return HttpResponse(f"user's session: {username}")

# 删除session
def del_session(request):
    # 1 删除指定的session
    # 删除的是浏览器的sessionid信息，如果delete()不带参数，默认删除的是浏览器的sessionid信息
    # request.session.delete('username')
    # 2 删除所有的session，flush()删除的是所有的sessionid信息
    request.session.flush()
    return HttpResponse('删除session')
```

### 使用session认证登录

```python
def login(request):
    error_msg = {'username':'', 'password':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'alex' and password == '123':
            # 先获取url中跳转的参数
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
        else:
            # 如果没有跳转的参数则直接跳转到首页
            obj = redirect('/home/')
        # cookie的过期时间 单位是秒  3600代表一个小时
        # obj.set_cookie('username', username, max_age=3600)

        # 设置session
        request.session['username'] = username
        request.session['ts'] = int(time.time())
        request.session.set_expiry(3600)

        return obj

    return render(request, 'login.html',{'error_msg': error_msg})


from functools import wraps

def login_auth(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        # 从request中获取cookie
        # print(request.path)
        # print(request.get_full_path())
        target_url = request.get_full_path()
        if request.session.get('username'):
            res = func(request,*args,**kwargs)
            return res
        else:
            return redirect('/login/?next=%s'%target_url)
    return inner

@login_auth
def home(request):
    username = request.session.get('username')
    return render(request, 'home.html',{'username': username})

def loginout(request):
    obj = redirect('/login/')
    request.session.flush()
    return obj

# 前端实现
## login.html
<form action="" method="post" enctype="application/x-www-form-urlencoded">
    <h2 class="h2">登陆</h2>
    <p>username: <input type="text" name="username"></p>
    <span  style="color: red">{{ error_msg.username }}</span>
    <p>password: <input type="password" name="password"></p>
    <span  style="color: red">{{ error_msg.password }}</span>
    <input type="submit">
</form>

## home.html
<h2>这是首页</h2>
<h3>欢迎用户{{ username }}登陆!!!</h3>
<button>
    <a href="/loginout/">注销</a>
</button>
```



## 中间件必会方法

django中间件
django中间件是类似于是django的保安,请求的时候需要先经过中间件才能到达django后端(urls,views,templates,models),响应走的时候也需要经过中间件才能到达web服务网关接口.

1.网站全局的身份校验,访问频率限制,权限校验...只要是涉及到全局的校验你都可以在中间件中完成 

2.django的中间件是所有web框架中 做的最好的

### 需要掌握的方法

### 1.process_request()方法

1. 请求来的时候 会经过每个中间件里面的process_request方法(从上往下)
2. 如果方法里面直接返回了HttpResponse对象那么会直接返回不再往下执行
   - 基于该特点就可以做访问频率限制,身份校验,权限校验。
     				
### 2.process_response()方法

1. 必须将response形参返回 因为这个形参指代的就是要返回给前端的数据
2. 响应走的时候 会依次经过每一个中间件里面的process_response方法(从下往上)

### 了解方法

### 1.process_view()

1. 在路由匹配成功执行视图函数之前触发。


### 2.process_exception()
1. 当你的视图函数报错时就会自动执行。
### 3.process_template_response()
1. 当你返回的HttpResponse对象中必须包含render属性才会触发。

```python
def index(request):
    print('我是index视图函数')
    def render():
        return HttpResponse('什么鬼玩意')
    obj = HttpResponse('index')
    obj.render = render
    return obj

```


中间件必须继承的类

```python
from django.utils.deprecation import MiddlewareMixin
```

定义中间件方法

```python
# mymiddleware/myadd.py
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class MyAdd(MiddlewareMixin):
    def process_request(self,request):
        print('我是第一个中间件里面的process_request方法')

    def process_response(self,request,response):
        print('我是第一个中间件的process_reponse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
        print('我是第一个中间件里面的process_view方法')

    def process_exception(self, request, exception):
        print('我是第一个中间件里面的process_exception')

    def process_template_response(self, request, response):
        print('我是第一个中间件里面的process_template_response')
        return response


class MyAdd1(MiddlewareMixin):
    def process_request(self, request):
        print('我是第2个中间件里面的process_request方法')

    def process_response(self, request, response):
        print('我是第2个中间件的process_reponse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
        print('我是第二个中间件里面的process_view方法')

    def process_exception(self, request, exception):
        print('我是第二个中间件里面的process_exception')

    def process_template_response(self, request, response):
        print('我是第二个中间件里面的process_template_response')
        return response


class MyAdd2(MiddlewareMixin):
    def process_request(self, request):
        print('我是第3个中间件里面的process_request方法')

    def process_response(self, request, response):
        print('我是第3个中间件的process_reponse方法')
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print(view_func)
        print(view_args)
        print(view_kwargs)
        print('我是第三个中间件里面的process_view方法')

    def process_exception(self, request, exception):
        print('我是第三个中间件里面的process_exception')

    def process_template_response(self, request, response):
        print('我是第三个中间件里面的process_template_response')
        return response

```

settings.py中引入，直接写路径

```python
MIDDLEWARE = [
......
    'mymiddleware.myadd.MyAdd',
    'mymiddleware.myadd.MyAdd1',
    'mymiddleware.myadd.MyAdd2',
]
```

## CSRF跨站伪造请求

原理：钓鱼网站通常模拟一个一模一样的页面来来误导用户，实际上提交的信息是被篡改过的信息；通过csrf token的方式给页面做标记，当钓鱼网站中向后端发送的csrf token标识不合法的时候后端服务器就可以直接拒接提交的非法的请求。

csrf token有以下特点

1. 同一个浏览器每一次访问都不一样
2. 不同浏览器绝对不会重复

settings.py中csrf的配置

```python
MIDDLEWARE = [
......
    'django.middleware.csrf.CsrfViewMiddleware',
......
]
```



### 1.FORM发送请求携带csrf

```python
# 直接携带
{% csrf_token %}

# login.html
<form action="" method="POST">
    {% csrf_token %}
    <p>username: <input type="text" name="username"></p>
    <p>password: <input type="password" name="password"></p>
    <input type="submit">
</form>
```



### 2.ajax携带csrf

#### 2.1 在ajax中通过标签获csrf token

```html
<form action="" method="POST">
    {% csrf_token %}
    <p>username: <input type="text" name="username"></p>
    <p>password: <input type="password" name="password"></p>
    <input type="submit">
    <button id="b1">发送ajax请求</button>
</form>
<script>
        $('#b1').click(function () {
            $.ajax({
                url: '',
                type: 'post',
                // 第一种方式
                data: {'username': 'jason', 'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()},
                // 第二种方式
                // data: {'username': 'jason', 'csrfmiddlewaretoken': '{{ csrf_token }}'},
                // 第三种方式 :直接引入js文件
                // data: {'username': 'jason'},
                success: function (data) {
                    alert(data)
                }
            })
        })

</script>
```



#### 2.2 直接ajax的模板中声名

```html
<form action="" method="POST">
    {% csrf_token %}
    <p>username: <input type="text" name="username"></p>
    <p>password: <input type="password" name="password"></p>
    <input type="submit">
    <button id="b1">发送ajax请求</button>
</form>
<script>
        $('#b1').click(function () {
            $.ajax({
                url: '',
                type: 'post',
                // 第一种方式
                // data: {'username': 'jason', 'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()},
                // 第二种方式
                data: {'username': $('[name=username]').val(), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
                // 第三种方式 :直接引入js文件
                // data: {'username': 'jason'},
                success: function (data) {
                    alert(data)
                }
            })
        })
</script>
```

#### 2.3 把获取csrf toekn封装到js中

```js
// static/csrf.js
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});
```

在form表单中直接引入

```html
<form action="" method="POST">
    {% csrf_token %}
    <p>username: <input type="text" name="username"></p>
    <p>password: <input type="password" name="password"></p>
    <input type="submit">
    <button id="b1">发送ajax请求</button>
</form>
{% load static %}
<script src="{% static 'csrf.js' %}"></script> <!--引入对csrf的处理js-->
<script>
        $('#b1').click(function () {
            $.ajax({
                url: '',
                type: 'post',
                // 第一种方式
                // data: {'username': 'jason', 'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()},
                // 第二种方式
                // data: {'username': $('[name=username]').val(), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
                // 第三种方式 :直接引入js文件

                data: {'username': $('[name=username]').val()},
                success: function (data) {
                    alert(data)
                }
            })
        })
</script>
```

### 3.局部使用csrf校验

单个保护或者是不保护是根据是否在settings.py中启用csrf相对的。如果启用就是`@不保护`，反之就是`@保护`

#### 3.1 在fbv中使用

```python
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# 不保护
@csrf_exempt
def login(request):
    return HttpResponse('login')

# 保护
@csrf_protect
def lll(request):
    return HttpResponse('lll')
```



#### 3.2 在cbv中使用

```python
from django.views import View
from django.utils.decorators import method_decorator

# 第一中种方式
# @method_decorator(csrf_protect,name='post')  # 有效的
# @method_decorator(csrf_exempt,name='post')  # 无效的
@method_decorator(csrf_exempt,name='dispatch')  # 第二种可以不校验的方式
class MyView(View):
    # @method_decorator(csrf_exempt)  # 第一种可以不校验的方式
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        res = super().dispatch(request, *args, **kwargs)
        return res

    def get(self,request):
        return HttpResponse('get')
    # 第二种方式
    # @method_decorator(csrf_exempt)  # 无效的
    # @method_decorator(csrf_protect)  # 有效的
    def post(self,request):
        return HttpResponse('post')
```

## Auth方法

如果你想用auth模块那么就要使用全套。
跟用户相关的功能模块:
- 用户的注册
- 登陆
- 验证
- 修改密码 ...

执行数据库迁移命令之后会生成很多表其中的auth_user是一张用户相关的表格.

添加数据
```python
python manage.py createsuperuser admin
```
创建超级用户这个超级用户就可以拥有登陆django admin后台管理的权限.

### 1.使用auth认证

urls.py

```python
path('auth_login/',views.auth_login, name='auth_login')
```

auth_login.html

```html
<form action="" method="POST">
    {% csrf_token %}
    <p>username: <input type="text" name="username"></p>
    <p>password: <input type="password" name="password"></p>
    <input type="submit">
</form>
```

views.py

```python
def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 必须要用因为数据库中的密码字段是密文的而你获取的用户输入的是明文
        user = auth.authenticate(username=username,password=password)
        # 没有查询到用户返回的是none
        print(user)
        if user:
            # 将用户状态记录到session中
            """只要执行了这一句话  你就可以在后端任意位置通过request.user获取到当前用户对象"""
            auth.login(request,user)
            return HttpResponse('登陆成功!')
        else:
            return HttpResponse('登陆失败!')
    return render(request,'auth_login.html')
```

### 2.判断用户是否登录

```python
# urls.py
path('is_login/',views.is_login, name='is_login')

# 判断用户是否登陆的方法实现
def is_login(request):
    # 获取当前用户对象
    user = request.user
    # 判断用户是否登陆,如果没有登陆user的值就是AnonymousUser
    authtked = request.user.is_authenticated
    print(user, authtked)

    # 判断用户是否登陆
    if authtked:
        return HttpResponse(f'{user}用户已经登陆!')
    else:
        return HttpResponse(f'用户未登陆! {user}')
```

### 3.校验登陆访问

```python
# 登陆访问成功后,跳转到指定的页面
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login_required/')  # 局部配置
@login_required(login_url='/auth_login/')
def user_detail(request):
    user = request.user
    return HttpResponse(f'这是用户{user}的详情页!')

# 处理GET next参数,在认证方法中实现
...
            if request.GET.get('next'):
                print(request.GET.get('next'))
                return redirect(request.GET.get('next'))
...

# 在全局范围内定义登陆跳转页面
## settings.py
LOGIN_URL = '/xxx/'
```

### 4.修改用户密码

```python
# alter_password.html
<form action="" method="POST">
    {% csrf_token %}
    <p>username: <input type="text" name="username" value="{{ username }}" disabled></p>
    <p>old password: <input type="password" name="old_pas"></p>
    <p>new password: <input type="password" name="new_pas"></p>
    <input type="submit">
</form>


# 修改密码需要用户登陆
@login_required(login_url='/auth_login/')
def alter_password(request):
    user = request.user
    if request.method == 'POST':
        old_pas = request.POST.get('old_pas')
        new_pas = request.POST.get('new_pas')
        # 校验旧密码是否正确
        if user.check_password(old_pas):
            # 修改密码
            user.set_password(new_pas)
            user.save()
            # 修改密码成功之后注销当前用户状态
            auth.logout(request)
            return HttpResponse('密码修改成功!')
        else:
            return HttpResponse('密码修改失败!')
    return render(request, 'alter_password.html',{'username': user})
```





### 5.注册用户

- 普通用用户

- 管理员用户

```python
# templates/register.html
<form action="" method="POST">
    {% csrf_token %}
    <label>
      <p>是否为管理员: <input type="checkbox" name="is_superuser" value="true"></p>
    </label>
    <p>username: <input type="text" name="username"></p>
    <p>password: <input type="password" name="password"></p>
    <p>email: <input type="text" name="email"></p>
    <input type="submit">
</form>

# urls.py
path('register/',views.register, name='register'),

# views.py
from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        is_superuser = request.POST.get('is_superuser')
        print(is_superuser)
        if is_superuser:
            # 创建管理员用户,email为必填字段
            User.objects.create_superuser(username=username,password=password,email=email)
        else:
            # 创建普通用户
            User.objects.create_user(username=username,password=password,email=email)
        return HttpResponse(f'{username} 注册成功!')

    return render(request,'register.html')
```

## auth用户自定义表

```python
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    """
    自定义用户表
    """
    phone = models.BigIntegerField(null=True, blank=True)
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.png')
    
# 一定要告诉django使用的是自定义的表 settings.py
# app.类名称
AUTH_USER_MODEL = 'app01.UserInfo'

# 迁移表
python manage.py makemigrations
python manage.py migrate
```



## django思想功能插拔式配置

核心思想，把每个功能都写在一个包中，通过鸭子模型和反射，定义每个功能中都有相似的方法，通过settings.py列出每个包中的功能，在包的`__init__.py`中通过for循环导入settings.py中的配置项来处理每个功能，这样如果在settings.py中功能被注释了那么就不会被处理。这样实现了功能的热配置。

见day59/hotsetframework部分代码。

```python
# hotsetframework/
```





## UI

- Layui
- AdminLTE
- tailwandcss