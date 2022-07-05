from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import SET_NULL


class TypeCompany(models.Model):
    name = models.CharField('Тип компании', max_length=300)

    def __str__(self):
        return '{}'.format(self.name)


class Brand(models.Model):
    name = models.CharField('Бренд', max_length=300)
    type_company = models.ForeignKey(TypeCompany, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Type(models.Model):
    name = models.CharField('Тип мыши', max_length=300)

    def __str__(self):
        return '{}'.format(self.name)


class Connector(models.Model):
    name = models.CharField('Connector', max_length=300)

    def __str__(self):
        return '{}'.format(self.name)


class Model(models.Model):
    name = models.CharField('Модель', max_length=300)
    generation = models.CharField('Поколение', max_length=300)
    type = models.ForeignKey(Type, on_delete=SET_NULL, null=True, blank=True)
    connector = models.ForeignKey(Connector, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    price = models.FloatField(verbose_name='Цена')
    brand = models.ForeignKey(Brand, on_delete=SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=SET_NULL, null=True, blank=True)
    description = RichTextField(verbose_name='Описание')
    data = models.DateTimeField(verbose_name='Дата выпуска')
    image = models.ImageField(null=True, verbose_name='Картинка', blank=True)
    available = models.BooleanField(default=False, verbose_name='Доступность')

    def __str__(self):
        return '{}{}{}'.format(self.brand, self.model, self.price)

    class Meta:
        verbose_name = 'Мышь'
        verbose_name_plural = 'Мыши'

    def get_absolute_url(self):
        return f'/market/{self.id}'