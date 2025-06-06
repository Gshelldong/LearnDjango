from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
from app01 import models

# Create your views here.
def index(request):
    if request.is_ajax():
        if request.method == 'POST':
            v1 = request.POST.get('i1')
            v2 = request.POST.get('i2')
            v3 = int(v1) + int(v2)

            return HttpResponse(v3)

    return render(request,'index.html')

def form(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            return HttpResponse('收到了')
    return render(request, 'form.html')


def test(request):
    print(request.body)
    print(request.content_type)

    return render(request, 'test.html')


def listbook(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 100, 'msg': ''}
            book_id = request.POST.get('id')
            print(book_id)
            models.Book.objects.filter(pk=book_id).delete()
            back_dic['msg'] = '真的删除了!'

            return JsonResponse(back_dic)
    books = models.Book.objects.all()
    # res = serializers.serialize('json', books)
    return render(request, 'listbook.html', locals())

