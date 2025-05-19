from django.urls import path

from .views import *
from . import views


categories_get_all_api = CategoriesMVS.as_view({
    'get': 'categories_get_all_api',
})

urlpatterns = [
    path('categories_get_all_api/', categories_get_all_api, name='categories_get_all_api'),
]