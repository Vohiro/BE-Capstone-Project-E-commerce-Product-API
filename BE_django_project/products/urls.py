from django.urls import path
from .views import (
    ListProduct,
    DetailProduct,
)

urlpatterns = [
    path('products/', ListProduct.as_view(), name='product_list'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='product_detail'),
]