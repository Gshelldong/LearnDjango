import os

from django.test import TestCase

# Create your tests here.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day54.settings')

import django
django.setup()

from app01 import models

# 查
# print(models.Book.objects.all())

# 增加数据
# 方法一：
# book_obj = models.Book.objects.create(title='红楼梦',price=150,create_time='2025-05-18')
# print(book_obj.title)

# 方法二：
# from datetime import datetime
# ctime = datetime.now()
# book_obj = models.Book(title='十万个为什么',price=98,create_time=ctime)
# book_obj.save()

# 条件查询
# print(models.Book.objects.filter(id=1))
# print(models.Book.objects.get(id=1))
# print(models.Book.objects.get(pk=1))

# 修改数据
# models.Book.objects.filter(pk=1).update(price='88') # 修改价格为88
# 或者
# book_obj = models.Book.objects.get(pk=2)
# book_obj.price = 71 # 修改价格为71
# book_obj.save()


# 删除数据
# models.Book.objects.filter(pk=2).delete()

# 条件查询
# 它包含了与所给筛选条件相匹配的对象
# print(models.Book.objects.filter(pk=1))

# 返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
# print(models.Book.objects.get(pk=1))

# 反向查询
# 它包含了与所给筛选条件不匹配的所有对象
# print(models.Book.objects.exclude(pk=1))

# 查询结果排序
# print(models.Book.objects.order_by('price'))
# print(models.Book.objects.order_by('-price'))

# 对结果反向排序，需要现有排序才行
# print(models.Book.objects.order_by('price').reverse())

# 统计查询结果条数
# print(models.Book.objects.filter(title='西游记').count())

# 查询返回结果的第一条和最后一条
# print(models.Book.objects.all().first())
# print(models.Book.objects.all().last())

# 判断是否有返回结果
# print(models.Book.objects.filter(pk=1).exists())

# 查询特定字段
# 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
# model的实例化对象，而是一个可迭代的字典序列
# 得到的结果是列表套字典
# print(models.Book.objects.values('title', 'price'))

# 查询特定字段返回列表
# print(models.Book.objects.values_list('title', 'price'))

# 对查询的返回结果进行去重，内容必须是一样的才行
print(models.Book.objects.values('title').distinct())