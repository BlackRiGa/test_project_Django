from django.db import models


# Create your models here.
class Car(models.Model):
    price = models.FloatField(verbose_name='Цена')
    brand = models.CharField(verbose_name='Бренд', default='', max_length=300)
    model = models.CharField(verbose_name='Модель', default='', max_length=300)
    description = models.TextField(verbose_name='Описание')
    data = models.DateTimeField(verbose_name='Дата выпуска')

    def __str__(self):
        return '{}{}{}'.format(self.brand, self.model, self.price)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
