from django.shortcuts import render,HttpResponse,reverse


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
