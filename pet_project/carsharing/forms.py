from django.conf import settings

from .models import Car
from django.forms import ModelForm, TextInput, DateTimeInput, FloatField, Textarea, DateInput, DateField


class CarForm(ModelForm):


    class Meta:
        model = Car
        fields = ['price', 'brand', 'model', 'description', 'data']

        widgets = {
            'brand': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Бренд',
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'data': DateInput(format='dd.mm.yyyy', attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            })
        }
