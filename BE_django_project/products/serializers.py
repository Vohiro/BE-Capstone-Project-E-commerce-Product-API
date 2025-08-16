from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'name',
            'description',
            'image',
            'category',
            'price',
            'stock_quantity',
            'available',
            'created_date',
        ]

        model = Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'name',
        ]

        model = Category