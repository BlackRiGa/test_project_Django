# Generated by Django 3.2.12 on 2022-03-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('brand', models.CharField(default='', max_length=300, verbose_name='Бренд')),
                ('model', models.CharField(default='', max_length=300, verbose_name='Модель')),
                ('description', models.TextField(verbose_name='Описание')),
                ('data', models.DateTimeField(verbose_name='Дата выпуска')),
            ],
        ),
    ]
