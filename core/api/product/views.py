from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q, Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.forms.models import model_to_dict
import re
from rest_framework.parsers import MultiPartParser, FormParser

from api.models import *
from .serializers import *
from api import status_http

class ProductsMVS(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    @action(methods=['GET'], detail=False, url_name='products_get_all_api', url_path='products_get_all_api')
    def products_get_all_api(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializers = self.serializer_class(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    @action(methods=['GET'], detail=False, url_name='top_expensive_products', url_path='top_expensive_products')
    def top_expensive_products(self, request, *args, **kwargs):
        top_products = Product.objects.order_by('-price_new')[:4]
        serializer = self.serializer_class(top_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)