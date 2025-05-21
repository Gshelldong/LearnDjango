from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_date = models.DateField(auto_now_add=True)
    kucun = models.IntegerField(null=True)
    maichu = models.IntegerField(null=True)

    # 默认和Publish表的主键为外键
    publish = models.ForeignKey(to="Publish",on_delete=models.CASCADE)
    # 虚拟字段，自动创建第三张表，帮助orm跨表查询
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title

class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    # varchar 254
    email = models.EmailField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDetail',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

    def __str__(self):
        """
        str 方法必须返回一个字符串
        :return:
        """
        return self.addr

