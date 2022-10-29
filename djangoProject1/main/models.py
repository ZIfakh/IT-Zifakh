from django.db import models
from datetime import datetime


# Create your models here.

def default_datetime(): 
    return datetime.now()

class CalcsHistory(models.Model):

    id = models.AutoField(primary_key=True)
    val1 = models.IntegerField(default=0, verbose_name='Первое значение')
    val2 = models.IntegerField(default=0, verbose_name='Второе значение')
    created_at = models.DateTimeField(default=default_datetime)
    result = models.IntegerField(default=None, verbose_name='Результат')
    operator = models.CharField(max_length=1, verbose_name='Оператор')


    def __str__(self):
        return f'Id:{self.id}'

