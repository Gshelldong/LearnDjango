import os

from django.test import TestCase

# Create your tests here.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day55.settings')

import django
django.setup()

from app01 import models

# 增加一本书籍指定出版社。
# models.Book.objects.create(title='钢铁是怎样练成的',price='50.32',publish_date='2025-05-04',publish_id=5)

# publish_obj = models.Publish.objects.filter(id=1).first()
# print(publish_obj)
# models.Book.objects.create(title='三国演义',price='154',publish_date='2015-07-01',publish=publish_obj)

# 修改书籍的出版社信息
# models.Book.objects.filter(title='Java核心技术').update(publish_id = 3)

# publish_obj = models.Publish.objects.filter(id=2).first()
# models.Book.objects.filter(title='Java核心技术').update(publish=publish_obj)

# 删除出版社
# models.Publish.objects.filter(pk=1).delete()

# 多对多的增删改查
# 给书籍钢铁是怎样练成的添加两个作者
# book_obj = models.Book.objects.filter(title='钢铁是怎样练成的').first() # type: models.Book
# book_obj.authors.add(9,10) # 直接使用作者表的主键id

# author1 = models.Author.objects.filter(id=5).first()
# author2 = models.Author.objects.filter(id=6).first()
# book_obj = models.Book.objects.filter(pk=14).first() # type: models.Book
# book_obj.authors.add(author1,author2)

# 把java编程思想的作者修改为2,5
# book_obj = models.Book.objects.filter(title='Java编程思想').first() # type: models.Book
# author1 = models.Author.objects.filter(pk=2).first()
# author2 = models.Author.objects.filter(pk=5).first()
# book_obj.authors.set([author1, author2])

# 给书籍删除作者对象
# book_obj = models.Book.objects.filter(title='计算机图形学').first() # type: # models.Book
# book_obj.authors.remove(10)  # 删除id是10的作者id

# author1 = models.Author.objects.filter(pk=1).first()
# author2 = models.Author.objects.filter(pk=2).first()
# book_obj.authors.remove(author1,author2)

# 将某本书和作者的关系全部清空
# book_obj = models.Book.objects.filter(pk=5).first()
# book_obj.authors.clear()

# 查询书籍深度学习的出版社名称
# book_obj = models.Book.objects.filter(title='深度学习').first() # type: models.Book
# print(book_obj.publish.name)

# 查询书籍深度学习的作者
# book_obj = models.Book.objects.filter(title='深度学习').first() # type: models.Book
# authors, = book_obj.authors.all()
# print(authors.name)

# 查询作者王五的家庭地址
# author = models.Author.objects.filter(name='王五').first() # type: models.Author
# print(author.author_detail.addr)

# 查询北京大学出版社的出版的书籍
# publish_obj = models.Publish.objects.filter(name='北京大学出版社').first() # type: models.Publish
# books = publish_obj.book_set.all()
# for book in books:
#     print(book.title)

# 查询作者是jason写过的所有书籍pk是作者id
# author_obj = models.Author.objects.filter(pk=3).first() # type: models.Author
# books = author_obj.book_set.all()
# for book in books:
#     print(book.title)

# 查询电话号码13000130010的作者
# detail = models.AuthorDetail.objects.filter(phone=13000130010).first() # type: models.AuthorDetail
# print(detail.author.name)


# 查询书籍《数据库系统概念》的作者的电话号码
# book_obj = models.Book.objects.filter(title='数据库系统概念').first() # type: models.Book
# for auther in book_obj.authors.all(): # 这里返回的是一个列表所以要循环一下
#     print(auther.author_detail.phone)


# 查询钱七的手机号
# res = models.Author.objects.filter(name='钱七').values('author_detail__phone','author_detail__addr')
# print(res.first())

# 反向查询
# res1 = models.AuthorDetail.objects.filter(author__name='钱七').values('author__age')
# print(res1)

# 查询作者张三的年龄和手机号
# res = models.Author.objects.filter(name='张三').values('age', 'author_detail__phone')
# print(res)
# 反向查询
# res = models.AuthorDetail.objects.filter(author__name='张三').values('author__age', 'phone')
# print(res)

# 查询手机号码是13200132008的作者年龄和姓名
## 正向
# res = models.Author.objects.filter(author_detail__phone=13200132008).values('name', 'age')
# print(res)

## 反向
# res = models.AuthorDetail.objects.filter(phone=13200132008).values('author__name', 'author__age')
# print(res)

# 查询书籍id是1 的作者的电话号码
# 只要表里面有外键字段 你就可以无限制跨多张表
# res = models.Book.objects.filter(pk=7).values('authors__author_detail__phone')
# res1 = models.Book.objects.filter(pk=1).values('外键字段1__外键字段2__外键字段3__普通字段')
# print(res)

# 查询出版社为清华大学出版社的所有图书的名字和价格
# res = models.Publish.objects.filter(name='清华大学出版社').values('book__title','book__price')
# print(res)