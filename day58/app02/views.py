from django.shortcuts import render,HttpResponse
from django import forms


# Create your views here.
class LoginForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=3,label='用户名')  # 用户名最长八位最短三位
    password = forms.CharField(max_length=8, min_length=5, label='密码')  # 密码最长八位最短五位
    email = forms.EmailField()  # email必须是邮箱格式

def lg(request):
    form_obj = LoginForm()
    if request.method == 'POST':
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('ok')
    return render(request, 'lg.html', {'form_obj': form_obj})