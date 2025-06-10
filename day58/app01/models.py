from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to='Author', through='BooktoAuthor', through_fields=('book', 'author'))
    publication_date = models.DateField()
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(to='Book', through='BooktoAuthor', through_fields=('author', 'book'))
    # through 告诉django orm书籍表和作者表的多对多关系是通过BooktoAuthor来记录的
    # through_fields 告诉django orm记录关系时用过BooktoAuthor表中的book字段和author字段来记录的
    email = models.EmailField()
    def __str__(self):
        return self.name

class BooktoAuthor(models.Model):
    book = models.ForeignKey(to='Book',on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author',on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.book.title} - {self.author.name}'