from django.conf.urls import include
from django.urls import path

from rest_framework import permissions
from . import views
from .views import *

products_get_all_api = ProductsMVS.as_view({
    'get': 'products_get_all_api',
})

urlpatterns = [
    path('products_get_all_api/', products_get_all_api, name='products_get_all_api'),
]