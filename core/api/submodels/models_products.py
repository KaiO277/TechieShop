from django.db import models
from api.submodels.models_categories import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    price_new = models.DecimalField(max_digits=10, decimal_places=2)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    review = models.IntegerField(blank=True, null=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='detail')
    description = models.TextField()

    def __str__(self):
        return f"Detail of {self.product.name}"
