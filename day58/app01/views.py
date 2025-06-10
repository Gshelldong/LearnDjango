from django.shortcuts import render

# Create your views here.
def login(request):
    error_msg = {'username':'', 'password':''}
    if request.method == 'POST':
        username = request.POST.get('username')
        if '金瓶梅' in username:
            error_msg['username'] = '不能含有金瓶梅'
        password = request.POST.get('password')
        if len(password) < 3:
            error_msg['password'] = '密码不能小于3位'

    return render(request, 'login.html',{'error_msg': error_msg})


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