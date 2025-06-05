from django.shortcuts import render,HttpResponse
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
    books = models.Book.objects.all()
    res = serializers.serialize('json', books)
    return render(request, 'listbook.html', locals())

