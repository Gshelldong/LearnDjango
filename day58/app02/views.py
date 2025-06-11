from django.shortcuts import render,HttpResponse
from django import forms


# Create your views here.
class LoginForm(forms.Form):
    username = forms.CharField(max_length=8, min_length=3,label='用户名')  # 用户名最长八位最短三位
    password = forms.CharField(max_length=8, min_length=5, label='密码')  # 密码最长八位最短五位
    confirm_password = forms.CharField(max_length=8, min_length=5, label='确认密码')  # 确认密码最长八位最短五位
    email = forms.EmailField()  # email必须是邮箱格式

    # 单选的radio框
    gendenr = forms.ChoiceField(choices=[(1, '男'), (2, '女'), (3, '保密')], label='性别', initial=3,widget=forms.RadioSelect)

    # 单选select框
    hobby = forms.ChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好', initial=3,widget=forms.Select)

    # 多选的select框
    hobby1 = forms.MultipleChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好1', initial=[1, 3],widget=forms.SelectMultiple)

    # 单选的checkbox框
    hobby2 = forms.ChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好2', initial=3,widget=forms.CheckboxInput(attrs={'class': 'form-control haha'}))

    # 多选的checkbox框
    hobby3 = forms.MultipleChoiceField(choices=[(1, '篮球'), (2, '足球'), (3, '双色球')], label='爱好3', initial=[1, 3],widget=forms.CheckboxSelectMultiple)

    # 局部钩子函数用来验证用户名中的特俗字符
    def clean_username(self):
        # 钩子函数，验证用户名是否合法
        username = self.cleaned_data.get('username')
        if '666' in username:
            self.add_error('username', '用户名不能包含666')
        return username

    # 全局钩子函数用来验证密码是否一致
    def clean(self):
        # 钩子函数，验证密码是否一致
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data



def lg(request):
    form_obj = LoginForm()
    if request.method == 'POST':
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('ok')
    return render(request, 'lg.html', {'form_obj': form_obj})