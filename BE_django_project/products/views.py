from rest_framework import viewsets, permissions, filters
from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from accounts.permissions import IsAdminUserRole, IsReviewOwnerOrAdmin
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("category")
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserRole]

    # Enabling filtering, searching and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'category', 'category__name', 'available']
    search_fields = ['name', 'category__name']
    ordering_fields = ['name','created_date', 'price']
    ordering = ['-created_date'] 

    @action(detail=False, methods=['get'], url_path='search')
    def search_products(self, request):
        """Custom endpoint: /api/products/search/?q=keyword"""
        query = request.query_params.get('q', '')
        qs = self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(category__name__icontains=query)
        )
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    
    def get_queryset(self):
        qs = super().get_queryset()
        request = self.request

        # Category filter
        category = request.query_params.get('category')
        if category:
            if category.isdigit():
                qs = qs.filter(category_id=category)
            else:
                qs = qs.filter(category__name__icontains=category)

        # Price range filter
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)

        # Stock availability filter
        in_stock = request.query_params.get('in_stock')
        if in_stock == "true":
            qs = qs.filter(stock_quantity__gt=0)
        elif in_stock == "false":
            qs = qs.filter(stock_quantity__lte=0)

        return qs

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


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, IsReviewOwnerOrAdmin]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])

    def perform_create(self, serializer):
        product_id = self.kwargs["product_pk"]
        user = self.request.user

        # check if user already has a review for this product
        if Review.objects.filter(user=user, product_id=product_id).exists():
            from rest_framework.exceptions import ValidationError
            raise ValidationError("You have already reviewed this product.")

        serializer.save(user=user, product_id=product_id)
    
