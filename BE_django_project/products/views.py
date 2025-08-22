from rest_framework import viewsets, permissions, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django_filters import rest_framework
from accounts.permissions import IsAdminUserRole


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("category")
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserRole]

    # Enabling filtering, searching and ordering
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'created_date', 'category', 'available']
    search_fields = ['name', 'category__name']
    ordering_fields = ['name','created_date', 'price']
    ordering = ['-created_date'] 

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUserRole()]
        return [permissions.AllowAny()]        


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserRole]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUserRole()]
        return [permissions.AllowAny()]    
