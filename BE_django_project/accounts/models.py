from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def is_admin(self):
        return self.role == 'admin'

    def __str__(self):
        return self.username