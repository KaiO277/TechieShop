from rest_framework import serializers
from api.models import *
from api.submodels import *

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def add(self, request):
        try:
            name = self.validated_data['name']
            if Product.objects.filter(name=name).exists():
                print("ProductSerializer_add_error: Duplicate name")
                return None
            return Product.objects.create(**self.validated_data)
        except Exception as error:
            print("ProductSerializer_add_error:", error)
            return None

    def update(self, request):
        try:
            product = Product.objects.get(pk=self.validated_data['id'])
            for attr, value in self.validated_data.items():
                setattr(product, attr, value)
            product.save()
            return product
        except Product.DoesNotExist:
            return None
        except Exception as error:
            print("ProductSerializer_update_error:", error)
            return None

    def delete(self, request):
        try:
            product = Product.objects.get(pk=self.validated_data['id'])
            product.delete()
            return True
        except Exception as error:
            print("ProductSerializer_delete_error:", error)
            return None

class ProductDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProductDetail
        fields = '__all__'

    def add(self, request):
        try:
            return ProductDetail.objects.create(**self.validated_data)
        except Exception as error:
            print("ProductDetailSerializer_add_error:", error)
            return None

    def update(self, request):
        try:
            detail = ProductDetail.objects.get(pk=self.validated_data['id'])
            for attr, value in self.validated_data.items():
                setattr(detail, attr, value)
            detail.save()
            return detail
        except ProductDetail.DoesNotExist:
            return None
        except Exception as error:
            print("ProductDetailSerializer_update_error:", error)
            return None

    def delete(self, request):
        try:
            detail = ProductDetail.objects.get(pk=self.validated_data['id'])
            detail.delete()
            return True
        except Exception as error:
            print("ProductDetailSerializer_delete_error:", error)
            return None
