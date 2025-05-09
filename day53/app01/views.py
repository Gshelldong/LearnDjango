from django.shortcuts import render,HttpResponse,redirect,reverse
from app01 import models

# Create your views here.
def test(request,year):
    print("获取到了uri中的year: ",year)
    print(reverse('app01_test',args=(year,)))
    return HttpResponse(b'hello word!')

def test_named(request, year=None):
    print(year)
    print('rev: ', reverse('app01_test_named', kwargs={'year': 2029}))
    return HttpResponse('uri number is {}'.format(year))

def nameds(request, year=None,month=None,day=None):
    content = f'年{year},月{month},日{day}'
    print(content)
    return HttpResponse(content.encode('utf-8'))

def xxx(request,year):
    print(reverse('xxx', args=(year,)))
    return HttpResponse(b'hhhhhhhh')

def index(request,*args):
    print(reverse('app01_index',args=args))
    return render(request, 'index.html')

def login(request):
    print(reverse('app01_index'))
    return HttpResponse(b'hello login!')

def testadd(request):
    print(reverse('app01_test_named', kwargs={'year':1}))
    return HttpResponse(b'testadd')

def list_book(request):
    book_infos = models.Book.objects.all()
    return render(request, 'book_info.html', {'data': book_infos})

def add_book(request):
    if request.method == "POST":
        name = request.POST.get('bookname')
        price = request.POST.get('price')
        publish = request.POST.get('publish')
        publish = models.Publish.objects.filter(name=publish).first()
        book_obj = models.Book(title=name,price=price,publish=publish)
        book_obj.save()

        return redirect(reverse('book_info'))

    publishs = models.Publish.objects.all()
    return render(request, 'add_book.html', {'publishs': publishs})

def del_book(request, id):
    models.Book.objects.filter(id=id).delete()
    return  redirect(reverse('book_info'))

def edit_book(request, id):
    if request.method == 'POST':
        name = request.POST.get('bookname')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish')
        publish = models.Publish.objects.filter(id=publish_id).first()
        models.Book.objects.filter(id=id).update(title=name,price=price,publish=publish)

        return redirect(reverse('book_info'))

    book = models.Book.objects.filter(id=id).first()
    publishs = models.Publish.objects.all()
    return render(request,'edit_book.html',{'book': book,'publishs': publishs})
