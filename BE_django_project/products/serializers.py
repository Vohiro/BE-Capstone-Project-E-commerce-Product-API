from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'created_date',
            'updated_date'
        ]
        read_only_fields = [
            "id", 
            "slug",
            "created_date", 
            "updated_date"
            ]


class ProductSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source="category", read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'price',
            'category',
            'category_detail',
            'stock_quantity',
            'image',
            'available',
            'created_date',
            'updated_date'
        ]
        read_only_fields = [
            "id", 
            "slug",
            "created_date", 
            "updated_date"
            ]
        
    def validate_name(self, value: str) -> str:
        if not value or not value.strip():
            raise serializers.ValidationError("Name is required.")
        return value.strip()

    def validate_price(self, value):
        if value is None:
            raise serializers.ValidationError("Price is required.")
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_stock_quantity(self, value: int) -> int:
        if value is None:
            raise serializers.ValidationError("Stock Quantity is required.")
        if value < 0:
            raise serializers.ValidationError("Stock Quantity cannot be negative.")
        return value