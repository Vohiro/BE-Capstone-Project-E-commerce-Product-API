from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Category, Product

class ProductApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester",
        password="pass12345")
        self.category = Category.objects.create(name="Electronics",
        slug="electronics")
    def test_public_list_products(self):
        url = reverse("product-list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    def test_create_product_requires_auth(self):
        url = reverse("product-list")
        payload = {"name":"X","price":"10.00","category": self.category.id,
        "stock_quantity": 1}
        res = self.client.post(url, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_create_product_authenticated(self):
        self.client.force_authenticate(self.user)
        url = reverse("product-list")
        payload = {"name":"X","price":"10.00","category": self.category.id,
        "stock_quantity": 1}
        res = self.client.post(url, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
