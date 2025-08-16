from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'name',
            'category',
            'description',
            'available',
            'stock_quantity',
            'image',
            'created_date',
        ]

        model = Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'name',
        ]

        model = Category