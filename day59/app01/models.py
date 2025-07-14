from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    """
    自定义用户表
    """
    phone = models.BigIntegerField(null=True, blank=True)
    avatar = models.FileField(upload_to='avatars/', default='avatars/default.png')