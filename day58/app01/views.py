from django.http import HttpResponse
from django.shortcuts import render, redirect
import time


# Create your views here.
# def login(request):
#     error_msg = {'username':'', 'password':''}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         if '金瓶梅' in username:
#             error_msg['username'] = '不能含有金瓶梅'
#         password = request.POST.get('password')
#         if len(password) < 3:
#             error_msg['password'] = '密码不能小于3位'
#
#     return render(request, 'login.html',{'error_msg': error_msg})


def login(request):
    error_msg = {'username':'', 'password':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'alex' and password == '123':
            # 先获取url中跳转的参数
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
        else:
            # 如果没有跳转的参数则直接跳转到首页
            obj = redirect('/home/')
        # cookie的过期时间 单位是秒  3600代表一个小时
        # obj.set_cookie('username', username, max_age=3600)

        # 设置session
        request.session['username'] = username
        request.session['age'] = 18
        request.session['ts'] = int(time.time())
        request.session.set_expiry(3600)

        return obj

    return render(request, 'login.html',{'error_msg': error_msg})


from functools import wraps

def login_auth(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        # 从request中获取cookie
        # print(request.path)
        # print(request.get_full_path())
        target_url = request.get_full_path()
        if request.session.get('username'):
            res = func(request,*args,**kwargs)
            return res
        else:
            return redirect('/login/?next=%s'%target_url)
    return inner

@login_auth
def home(request):
    username = request.session.get('username')
    return render(request, 'home.html',{'username': username})

def detail(request):
    username = request.session.get('username')
    age = request.session.get('age')
    login_time = request.session.get('ts')
    login_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(login_time))
    return render(request, 'detail.html', locals())

def loginout(request):
    obj = redirect('/login/')
    request.session.flush()
    return obj


from django import forms
from django.core.validators import RegexValidator

class LoginForm(forms.Form):

    username = forms.CharField(max_length=8,min_length=3,initial='username',label='用户名',error_messages={
        'max_length': '用户名不能超过8位',
        'min_length': '用户名不能小于3位',
       'required': '用户名不能为空'
    },widget=forms.TextInput(attrs={'class': 'form-control haha'}))

    password = forms.CharField(max_length=8,min_length=3,label='密码',error_messages={
       'max_length': '密码不能超过8位',
       'min_length': '密码不能小于3位',
       'required': '密码不能为空'
    },widget=forms.PasswordInput(attrs={'class': 'form-control haha'}))

    confirm_password = forms.CharField(max_length=8,min_length=3,label='确认密码',error_messages={
      'max_length': '密码不能超过8位',
      'min_length': '密码不能小于3位',
      'required': '密码不能为空'
    },widget=forms.PasswordInput(attrs={'class': 'form-control haha'}),required=False,validators=[RegexValidator(r'^[0-9]+$', '请输入数字'),
                                   RegexValidator(r'^159[0-9]+$', '数字必须以159开头')])

    # email格式校验
    email = forms.EmailField(label='邮箱',error_messages={
      'required': '邮箱不能为空',
      'invalid': '邮箱格式不正确'
    })

def reg(request):
    # 1 现生成一个空的自定义类的对象
    form_obj = LoginForm()
    print(form_obj)
    # 2 将该对象传递给前端页面
    if request.method == 'POST':
        # 3 获取前端post请求提交过来的数据
        # print(request.POST)  # 由于request.POST其实也是一个字典 所有可以直接传给LoginForm
        form_obj = LoginForm(request.POST)
        # 4 校验数据  让forms组件帮你去校验
        if form_obj.is_valid():
            # 5 如果数据全部通过 应该写入数据库
            pass
        # 6 如果不通过 一个像前端展示错误信息
    return render(request,'re.html',locals())

def set_session(request):
    request.session['username'] = 'alex'
    request.session['age'] = 18
    request.session['ts'] = int(time.time())
    # 设置seession的超时时间是3600s
    # set_expiry(value)有几种情况
    # 1 如果value是一个整数，session将在这些秒数后到期。
    # 2 如果value是一个datatime或timedelta，session将在这个时间后到期。
    # 3 如果value是0,用户会话的Cookie将在用户的浏览器关闭时过期。
    # 4 如果value是None, session会使用全局session失效策略。
    # 5 设置小于0的整数，session将在会话的Cookie到期时过期。
    request.session.set_expiry(3600)
    return HttpResponse('设置session')

def get_session(request):
    username = request.session.get('username')
    age = request.session.get('age')
    ts = request.session.get('ts')

    print(username,age,ts)
    return HttpResponse(f"user's session: {username}")

# 删除session
def del_session(request):
    # 1 删除指定的session
    # 删除的是浏览器的sessionid信息，如果delete()不带参数，默认删除的是浏览器的sessionid信息
    # request.session.delete('username')
    # 2 删除所有的session，flush()删除的是所有的sessionid信息
    request.session.flush()
    return HttpResponse('删除session')