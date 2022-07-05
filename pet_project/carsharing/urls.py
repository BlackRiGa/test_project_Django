from django.urls import path
from . import views
from .api.views import CarAPIView

urlpatterns = [
    path('', views.cars, name='cars'),
    path('create/', views.create, name='create_car'),
    path('<slug:brand>/', views.car, name='car'),
    path('<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/update', views.CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete', views.CarDeleteView.as_view(), name='car_delete'),
    path('api/v1/car-list', CarAPIView.as_view()),
]
