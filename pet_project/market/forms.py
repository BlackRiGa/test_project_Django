
from .models import Product
from django.forms import ModelForm, TextInput, DateTimeInput, FloatField, Textarea, DateInput, DateField


class ProductForm(ModelForm):
    class Meta:
        model = Product
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
