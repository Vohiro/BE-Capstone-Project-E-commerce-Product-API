from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProductViewSet, 
    CategoryViewSet, 
    ReviewViewSet, 
    WishlistViewSet, 
    ProductImageViewSet
)
from rest_framework_nested import routers

# Main router
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'wishlists', WishlistViewSet, basename='wishlist')

# Nested router for reviews under products
products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'reviews', ReviewViewSet, basename='product-reviews')
products_router.register(r'images', ProductImageViewSet, basename='product-images')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
]

