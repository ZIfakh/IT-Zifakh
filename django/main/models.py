from django.db import models

# Create your models here.


class Car(models.Model):

    title = models.CharField(max_length=123, verbose_name='Название')
    year = models.IntegerField(null=True, verbose_name='Год')
    color = models.CharField(max_length=10, verbose_name='Цвет')


    def __str__(self):
        return self.title