from django.db import models

from accounts.models import CustomUser

SERVICES = [
    ('Товары', 'Товары'),
    ('Услуги', 'Услуги'),
]


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    date = models.DateField(verbose_name="Дата")
    image = models.FileField(upload_to='news', verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    city = models.CharField(max_length=255, verbose_name="Местоположение")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    services = models.CharField(max_length=255, verbose_name="Услуги", choices=SERVICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
