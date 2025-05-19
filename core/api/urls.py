from django.conf.urls import include
from django.urls import path

from rest_framework import permissions
from .views import *


urlpatterns = [
    path('categories/', include('api.categories.urls')),
    path('products/', include('api.product.urls')),
]