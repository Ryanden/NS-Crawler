from django.db import models
from django.conf import settings


# Create your models here.

class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=30)

    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):

    product_name = models.CharField(max_length=100)

    product_type = models.CharField(max_length=100)

    product_description = models.TextField(blank=True)
