from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name


