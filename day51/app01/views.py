from django.shortcuts import render,HttpResponse,redirect


# Create your views here.

# render 模板渲染
# HttpResponse 处理返回结果
# redirect  重定向

def home(request):
    return HttpResponse('网站主页')

def auth(request):
    print('POST: ',request.POST)
    if request.POST:
        print(request.POST.get('username'))
        if request.POST.get('username') == 'user' and request.POST.get('password') == '1':
            return HttpResponse('登陆成功 200')
        else:
            return HttpResponse('登陆失败 403')

def login(request):
    user_dict = {'name': 'json'}
    # 字典中的data就是模板中的data
    print(request)
    return render(request,'login.html',{'data': user_dict})

def rewriteurl(request):
    return redirect('/login')