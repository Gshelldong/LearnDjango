from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    create_time = models.DateField()  # 年月日
    # create_time = models.DateTimeField()  # 年月日 时分秒

    def __str__(self):
        return self.title