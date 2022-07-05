from django.db import models
from django.db.models import SET_NULL
from ckeditor.fields import RichTextField

class TypeCompany(models.Model):
    name = models.CharField('Тип компании', max_length=300)

    def __str__(self):
        return '{}'.format(self.name)


class Brand(models.Model):
    name = models.CharField('Бренд', max_length=300)
    type_company = models.ForeignKey(TypeCompany, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class BodyType(models.Model):
    name = models.CharField('Кузов', max_length=300)

    def __str__(self):
        return '{}'.format(self.name)


class Model(models.Model):
    name = models.CharField('Модель', max_length=300)
    generation = models.CharField('Поколение', max_length=300)
    date_from = models.DateTimeField('Выпускалась с')
    date_to = models.DateTimeField('Выпускалась до')
    body_type = models.ForeignKey(BodyType, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Light(models.Model):
    name = models.CharField('Название', max_length=300)
    power = models.IntegerField('Мощность')

    def __str__(self):
        return '{}'.format(self.name)


class Car(models.Model):
    price = models.FloatField(verbose_name='Цена')
    brand = models.ForeignKey(Brand, on_delete=SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=SET_NULL, null=True, blank=True)
    description = RichTextField(verbose_name='Описание')
    data = models.DateTimeField(verbose_name='Дата выпуска')
    image = models.ImageField(null=True, verbose_name='Картинка', blank=True)
    available = models.BooleanField(default=False, verbose_name='Доступность')

    light = models.ForeignKey(Light, on_delete=SET_NULL, null=True, blank=True, verbose_name='Тип света')

    def __str__(self):
        return '{}{}{}'.format(self.brand, self.model, self.price)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def get_absolute_url(self):
        return f'/carsharing/{self.id}'
