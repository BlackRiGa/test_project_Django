from django.conf import settings

from .models import Car
from django.forms import ModelForm, TextInput, DateTimeInput, FloatField, Textarea, DateInput, DateField, Select, FileInput
from django.forms.widgets import DateInput as WidgetDateInput


class CarForm(ModelForm):
    data = DateField(widget=WidgetDateInput(format='%m/%d/%Y'))

    class Meta:
        model = Car
        fields = ['price', 'brand', 'model', 'description', 'data', 'light', 'image']

        widgets = {
            'brand': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Бренд',
            }),
            'model': Select(attrs={
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
            }),
            'light': Select(attrs={
                'class': 'form-control',
            }),
            'image': FileInput()
        }
