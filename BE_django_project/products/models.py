from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    available = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_image', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['price']),
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.name
    
    # Optional future enhancement: stock deduction when an order is placed
    def reduce_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Quantity to reduce must be >= 0")
        if quantity > self.stock_quantity:
            raise ValueError("Insufficient stock")
        self.stock_quantity -= quantity
        self.save(update_fields=["stock_quantity"])

    def save(self, *args, **kwargs):
        # Convenience: auto-generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)