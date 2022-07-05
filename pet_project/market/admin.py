from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Product, Connector, Type, Model, Brand, TypeCompany


class DescriptionAdminForm (forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    form = DescriptionAdminForm
    list_display = ('brand', 'model', 'data', 'available', 'price', 'data',)
    list_display_links = ('brand', 'data')
    list_filter = ('brand', 'data', 'price')
    search_fields = ('description',)
    readonly_fields = ('get_image',)
    list_editable = ('available',)
    # fields = (('brand', 'model'),
    #           ('price', 'data'))

    fieldsets = (
        (None, {
            'fields': (('brand', 'model', 'available', 'price', 'data',),)
        }),
        ('Описание и цена', {
            # 'classes': ('collapse',),
            'fields': (('description', ),)
        }),
        ('Фото', {
            'fields': (('image', 'get_image'),)
        })
    )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} height="58" width="58">')
        return ''

    get_image.short_description = "Изображение"


admin.site.register(Product, ProductAdmin)
admin.site.register(TypeCompany)
admin.site.register(Type)
admin.site.register(Connector)
admin.site.register(Brand)
admin.site.register(Model)

