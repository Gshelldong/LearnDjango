from django.test import TestCase
import django
from django import forms

import os

# Create your tests here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day58.settings')
django.setup()

# 定义一个表单
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