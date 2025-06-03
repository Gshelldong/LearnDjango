from django.shortcuts import render,HttpResponse,redirect,reverse
from app01 import models

# Create your views here.

def home(request):
    return render(request,'home.html')

def list_book(request):
    book_allset = models.Book.objects.all()
    # authors = book_allset.authors.all()
    # print(authors)
    return render(request, 'list_book1.html', locals())

def user(request):
    user_allset = models.Author.objects.all()
    return render(request, 'author.html', locals())

def adduser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')
        # 添加作者
        author_summary = models.AuthorDetail.objects.create(phone=phone, addr=addr)
        models.Author.objects.create(name=name, age=age, author_detail=author_summary)

        return redirect(reverse('user'))

    return render(request,'adduser.html',locals())

def edit_user(request, edit_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        addr = request.POST.get('addr')

        models.Author.objects.filter(pk=edit_id).update(name=name, age=age)
        author_obj = models.Author.objects.filter(pk=edit_id).first() # type: models.Author
        author_obj_detail = author_obj.author_detail
        author_obj_detail.addr = addr
        author_obj_detail.phone = phone
        author_obj_detail.save()

        return redirect(reverse('user'))

    author = models.Author.objects.filter(pk=edit_id).first()
    return render(request,'edit_user.html',locals())


def publish(request):
    publish_allset = models.Publish.objects.all()
    return render(request, 'publish.html', locals())

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish = request.POST.get('publish')
        author = request.POST.get('author')
        book_obj = models.Book.objects.create(title=title,price=price,publish_date=publish_date,publish_id=publish)
        book_obj.authors.add(*author) # 多对多的关系要单独添加

        return redirect(reverse('listbook'))

    author_objs = models.Author.objects.all()
    publish_objs = models.Publish.objects.all()
    return render(request,'addbook.html', locals())

def edit_book(request, edit_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        publish_date = request.POST.get('publish_date')
        publish = request.POST.get('publish')
        author_ids = request.POST.getlist('author')

        models.Book.objects.filter(pk=edit_id).update(title=title, price=price, publish_date= publish_date, publish=publish)
        book_obj = models.Book.objects.filter(pk=edit_id).first() # type: models.Book
        book_obj.authors.set(author_ids)

        return redirect(reverse('listbook'))

    book = models.Book.objects.filter(pk=edit_id).first() # type: models.Book
    author_objs = models.Author.objects.all()
    publish_objs = models.Publish.objects.all()
    return render(request,'edit_book.html',locals())

def delete_book(request, delete_id):
    # 根据有名分组传递过来的id值 确定删除的数据对象
    # 1.简单粗暴 直接delete删除
    # 第一种
    # delete_obj = models.Book.objects.filter(pk=delete_id).first()
    # delete_obj.delete()
    # 第二种
    models.Book.objects.filter(pk=delete_id).delete()
    return redirect(reverse('listbook'))
    # 2.不直接删  给用户再次确认一次 问他是否真的要删

def search(request):
    search_title = request.GET.get('title')
    book_objs = models.Book.objects.filter(title__icontains=search_title).all()

    return render(request, 'search_book.html', locals())


