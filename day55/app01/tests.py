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