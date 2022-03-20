from django.urls import path
from . import views


urlpatterns = [
    path('', views.products, name='products'),
    path('create/', views.create, name='create_mouse')
]
