from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.
def login(request):
    # 视图函数针对不同的请求方式 应该有不同的处理逻辑
    # 针对POST方法做单独的处理，用户提交表单了，这样代码逻辑更加清晰，其它请求直接返回
    if request.method == 'POST':
        # getlist('username')获取这个属性的所有值
        user_name = request.POST.getlist('username')[0]
        password = request.POST.getlist('password')[0]
        # print(user_name, password)
        if user_name and password:
            # 查数据库
            user_obj = models.User.objects.filter(username=user_name).first()
            if user_obj:
                if user_obj.password == password:
                    return HttpResponse('登陆成功.')
            err_info = {'msg': 'username or password error'}
            return render(request, 'login.html', {'data': err_info})

    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST.getlist('username')[0]
        password = request.POST.getlist('password')[0]

        if user_name and password:
            user_obj = models.User(username=user_name,password=password)
            user_obj.save()

    return render(request, 'register.html')

def list_user(request):
    user_obj = models.User.objects.all()
    return render(request,'userinfo.html',{'data': user_obj})

def edit_user(request):
    user_id = request.GET.get('id')
    user_obj = models.User.objects.filter(id = user_id).first()
    if request.method == 'POST':
        username = request.POST.getlist('username')[0]
        password = request.POST.getlist('password')[0]
        # 更新数据库
        models.User.objects.filter(id = user_id).update(username=username, password=password)
        return redirect('/userinfo/')
    return render(request, 'edituser.html', {'data': user_obj})

def del_user(request):
    user_id = request.GET.get('id')
    models.User.objects.filter(id = user_id).delete()
    return redirect('/userinfo/')