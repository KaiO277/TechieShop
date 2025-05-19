from django.contrib import admin
from api.models import Category, Product, ProductDetail
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetail)
