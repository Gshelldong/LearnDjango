from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.
def test(request,year):
    print("获取到了uri中的year: ",year)
    return HttpResponse(b'hello word!')

def test_named(request, year=None):
    print(year)
    return HttpResponse('uri number is {}'.format(year))

def nameds(request, year=None,month=None,day=None):
    content = f'年{year},月{month},日{day}'
    print(content)
    return HttpResponse(content.encode('utf-8'))

def xxx(request,year):
    print(reverse('xxx', args=(1212,)))
    return HttpResponse(b'hhhhhhhh')