from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    stock_quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_image', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['-created_date']),
        ]

    def __str__(self):
        return self.name
    