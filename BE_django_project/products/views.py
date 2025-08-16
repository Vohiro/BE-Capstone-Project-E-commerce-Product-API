from rest_framework import generics, filters, status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters import rest_framework
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Pagination defined here (local to this view)
    class ProductPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        max_page_size = 100

    pagination_class = ProductPagination 
    

    # Enabling filtering, searching and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'created_date', 'category', 'available']
    search_fields = ['name', 'category__name', 'available']
    ordering_fields = ['name','created_date']
    ordering = ['created_date'] 


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
