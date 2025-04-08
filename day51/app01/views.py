from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def home(request):
    return HttpResponse('网站主页')

def auth(request):
    print(request)
    return HttpResponse('200')

def login(request):
    user_dict = {'name': 'json'}
    # 字典中的data就是模板中的data
    print(request)
    return render(request,'login.html',{'data': user_dict})



def rewriteurl(request):
    return redirect('/login')