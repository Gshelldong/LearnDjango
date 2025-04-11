from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
    # 视图函数针对不同的请求方式 应该有不同的处理逻辑
    # 针对POST方法做单独的处理，用户提交表单了，这样代码逻辑更加清晰，其它请求直接返回
    user_info = {'username': 'jerry'}
    if request.method == 'POST':
        # getlist('username')获取这个属性的所有值
        print(request.POST.getlist('username'))
    return render(request,'login.html',{'data': user_info})



