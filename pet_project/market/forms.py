from .models import Product
from django.forms import ModelForm, TextInput, DateTimeInput, FloatField, Textarea, Select, DateInput, DateField, FileInput
from django.forms.widgets import DateInput as WidgetDateInput


class ProductForm(ModelForm):
    data = DateField(widget=WidgetDateInput(format='%m/%d/%Y'))

    class Meta:
        model = Product
        fields = ['price', 'brand', 'model', 'description', 'data', 'image']

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
            'image': FileInput()
        }
