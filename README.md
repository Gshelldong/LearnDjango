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
pycharm快捷方式

**创建的应用一定要在settings中注册才能生效否则无法识别**

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

HttpResponse:返回字符串
render:返回html页面 并且能够给该页面传值
redirect:重定向


​	作业:
​		1.安装django  启动页面展示
​		2.用django展示数据库中的数据
​		3.登陆注册  集合数据库
​			(a标签)



