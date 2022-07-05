from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Car, Model, BodyType, Brand, TypeCompany, Light
from django import forms


class DescriptionAdminForm (forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Car
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):
    form = DescriptionAdminForm
    list_display = ('brand', 'model', 'data', 'available', 'price')
    list_display_links = ('brand', 'data')
    list_filter = ('brand', 'data', 'price')
    search_fields = ('description',)
    readonly_fields = ('price', 'get_image')
    list_editable = ('available', )
    # fields = (('brand', 'model'),
    #           ('price', 'data'))

    fieldsets = (
        (None, {
            'fields': (('brand', 'model', 'available', 'light'),)
        }),

        ('Описание и цена', {
            # 'classes': ('collapse',),
            'fields': (('description', 'price',),)
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


admin.site.register(Car, CarAdmin)
admin.site.register(Light)
admin.site.register(Model)
admin.site.register(TypeCompany)
admin.site.register(BodyType)
admin.site.register(Brand)


