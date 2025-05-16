from django.shortcuts import render,HttpResponse,redirect
from django.http import  JsonResponse
from django.views import View


# Create your views here.

def index(request):
    return render(request,'index.html',{'data':'hell oword!'})

from django.template import Template,Context
def red(request):
    temp = Template('<h1>{{ user }}</h1>')
    con = Context({"user":{"name":'jason',"password":'123'}})
    res = temp.render(con)
    print(res)
    return HttpResponse(res)

class MyLogin(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self, request):
        print(request.POST.get('username'))
        return HttpResponse('成功')
