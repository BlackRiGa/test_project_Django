from django.urls import path
from . import views


urlpatterns = [
    path('', views.cars, name='cars'),
    path('create/', views.create, name='create_car'),
    path('<slug:brand>/', views.car, name='car')
]
