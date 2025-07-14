from django.shortcuts import render, HttpResponse, reverse, redirect


# Create your views here.

def home(request):
    return HttpResponse('这是主页home!')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        return HttpResponse(f'{username} 登陆成功!')
    return render(request,'login.html')


from django.views.decorators.csrf import csrf_exempt,csrf_protect

@csrf_protect
def pay(request):
    if request.method == 'POST':
        pay_num = request.POST.get('pay_num')
        print(f'支付了{pay_num}')
        return HttpResponse('支付成功!')
    return render(request,'pay.html')


from django.contrib import auth

def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 必须要用因为数据库中的密码字段是密文的而你获取的用户输入的是明文
        user = auth.authenticate(username=username,password=password)
        # 没有查询到用户返回的是none
        print(user)
        if user:
            # 将用户状态记录到session中
            """只要执行了这一句话  你就可以在后端任意位置通过request.user获取到当前用户对象"""
            auth.login(request,user)
            if request.GET.get('next'):
                print(request.GET.get('next'))
                return redirect(request.GET.get('next'))
            return HttpResponse('登陆成功!')
        else:
            return HttpResponse('登陆失败!')
    return render(request,'auth_login.html')

def is_login(request):
    # 获取当前用户对象
    user = request.user
    # 判断用户是否登陆,如果没有登陆user的值就是AnonymousUser
    authtked = request.user.is_authenticated
    print(user, authtked)

    # 判断用户是否登陆
    if authtked:
        return HttpResponse(f'{user}用户已经登陆!')
    else:
        return HttpResponse(f'用户未登陆! {user}')

# 登陆访问成功后,跳转到指定的页面
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login_required/')  # 局部配置
@login_required(login_url='/auth_login/')
def user_detail(request):
    user = request.user
    return HttpResponse(f'这是用户{user}的详情页!')

@login_required(login_url='/auth_login/')
def alter_password(request):
    user = request.user
    if request.method == 'POST':
        old_pas = request.POST.get('old_pas')
        new_pas = request.POST.get('new_pas')
        # 校验旧密码是否正确
        if user.check_password(old_pas):
            # 修改密码
            user.set_password(new_pas)
            user.save()
            # 修改密码成功之后注销当前用户状态
            auth.logout(request)
            return HttpResponse('密码修改成功!')
        else:
            return HttpResponse('密码修改失败!')
    return render(request, 'alter_password.html',{'username': user})

from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        is_superuser = request.POST.get('is_superuser')
        print(is_superuser)
        if is_superuser:
            # 创建管理员用户
            User.objects.create_superuser(username=username,password=password,email=email)
        else:
            # 创建普通用户
            User.objects.create_user(username=username,password=password,email=email)
        return HttpResponse(f'{username} 注册成功!')

    return render(request,'register.html')
