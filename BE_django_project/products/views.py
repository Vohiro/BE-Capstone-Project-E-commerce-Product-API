from rest_framework import generics, filters, status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters import rest_framework
from rest_framework.response import Response


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Enabling filtering, searching and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'created_date', 'category', 'available']
    search_fields = ['name', 'category__name', 'available']
    ordering_fields = ['name','created_date']
    ordering = ['created_date'] 


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
