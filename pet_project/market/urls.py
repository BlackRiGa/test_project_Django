from django.urls import path
from . import views
from .api.views import ProductRetriveUpdateDestroy, ProductListCreate

urlpatterns = [
    path('', views.products, name='products'),
    path('create/', views.create, name='create_product'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('<int:pk>/update', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', views.ProductDeleteView.as_view(), name='product_delete'),
    path('api/v1/product-list', ProductListCreate.as_view(), name='product_detail_view'),
    path('api/v1/product-list/<int:pk>', ProductRetriveUpdateDestroy.as_view(), name='product_detail_view'),
]
