from django.conf.urls import include
from django.urls import path

from rest_framework import permissions
from . import views
from .views import *

products_get_all_api = ProductsMVS.as_view({
    'get': 'products_get_all_api',
})

top_expensive_products = ProductsMVS.as_view({
    'get': 'top_expensive_products',
})


urlpatterns = [
    path('products_get_all_api/', products_get_all_api, name='products_get_all_api'),
    path('top_expensive_products/', top_expensive_products, name='top_expensive_products'),
]