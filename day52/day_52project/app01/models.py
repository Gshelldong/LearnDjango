from django.db import models

# Create your models here.
class User(models.Model):
    # User表的映射关系
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField(null=True)
    addr = models.CharField(max_length=32, default='China')
    describe = models.CharField(max_length=64)

username = 'band'
password='qwer123'
describe = 'robot'
addr = 'usa'
age = 34