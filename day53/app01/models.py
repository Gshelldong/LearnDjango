from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Book(models.Model):
    # id自动创建 可以不写
    title = models.CharField(max_length=64)
    # 共8位 小数部分占两位
    price = models.DecimalField(max_digits=8,decimal_places=2)

    # 书籍和出版社是一对多的外键关系
    publish = models.ForeignKey(to='Publish')  # to表示的就是跟哪张表是一对多的关系   默认都是跟表的主键字段建立关系
    """
    只要是ForeignKey的字段 django orm在创建表的时候 会自动在一对多的字段名之后加_id
    如果你自己加了 不管 还会继续往后加
    """
    # publish = models.ForeignKey(to=Publish)  # to后面也可以直接写表名 但是必须保证表名在上面
    # 书籍和作者是多对多的关系
    # 不会在表中生成authors字段 该字段是一个虚拟字段 仅仅是用来告诉django orm自动帮你创建书籍和作者的第三张关系表
    authors = models.ManyToManyField(to='Author')

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 作者与作者详情 是一对一的外键关系
    author_detail = models.OneToOneField(to='AuthorDetail',null=True)
    """
    也会自动再字段名后面加_id
    """

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=32)


