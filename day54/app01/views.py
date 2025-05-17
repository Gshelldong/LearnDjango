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

def reg(request):
    # 先验证是否python所有的数据类型都可以被传递到前端
    n = 0
    # ss = ''
    f = 1.11
    s = '你妹的'
    l = [1,2,3,4,5,6,[12,3,4,{'name':'heiheihei'}]]
    d = {"name":'jason','password':123}
    t = (1,2,3,4,5)
    se = {1,2,3,4,5,6,7,}
    file_size = 12312312

    info = 'my name is jason and my age is 18'
    info1 = '傻大姐 撒旦 技术 大 萨达 了 奥斯卡 的健康两 三点卡是考虑到'
    def index(xxx):
        print(xxx)
        print('index')
        return '我是index函数的返回值'

    class Demo(object):
        def get_self(self):
            return '绑定给对象的方法'
        @classmethod
        def get_cls(cls):
            return '绑定给类的方法'
        @staticmethod
        def get_static():
            return '我是静态方法其实就是函数'
    obj = Demo()

    # 给模板传值的方式
    # 方式1
    # 通过字典的键值对 指名道姓的一个个的传
    # return render(request,'reg.html',{'n':n,'f':f})
    # 方式2
    # locals会将它所在的名称空间中的所有的名字全部传递给前端
    # 该方法虽然好用 但是在某些情况下回造成资源的浪费
    xxx = '<h1>波波棋牌室</h1>'

    yyy = '<script>alert(123)</script>'
    from django.utils.safestring import mark_safe

    zzz = mark_safe('<h1>阿萨德搜啊第三款垃圾袋</h1>')


    from datetime import datetime
    ctime = datetime.now()

    return render(request,'index.html',locals())  # 为了教学方便 我们以后就用locals()

def home(request):
    return  render(request,'home.html')

def register(request):
    return render(request,'register.html')