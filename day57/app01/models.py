from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    choice = [
        (1,'男'),
        (2,'女'),
        (3,'其它'),
    ]
    gender = models.IntegerField(choices=choice)

    def __str__(self):
        return self.username


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="书籍名称")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="价格")
    author = models.CharField(max_length=50, verbose_name="作者")
    publisher = models.CharField(max_length=100, verbose_name="出版社")
    description = models.TextField(blank=True, null=True, verbose_name="描述")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = "图书管理"