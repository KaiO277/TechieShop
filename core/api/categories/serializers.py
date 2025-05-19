from rest_framework import serializers
from api.models import *
from api.submodels import *

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = '__all__'

    def add(self, request):
        try:
            name = self.validated_data['name']
            if Category.objects.filter(name=name).exists():
                print("CategorySerializer_add_error: Duplicate name")
                return None
            return Category.objects.create(name=name)
        except Exception as error:
            print("CategorySerializer_add_error:", error)
            return None

    def update(self, request):
        try:
            category_id = self.validated_data['id']
            name = self.validated_data['name']

            category = Category.objects.get(pk=category_id)
            category.name = name
            category.save()
            return category
        except Category.DoesNotExist:
            return None
        except Exception as error:
            print("CategorySerializer_update_error:", error)
            return None

    def delete(self, request):
        try:
            category = Category.objects.get(pk=self.validated_data['id'])
            category.delete()
            return True
        except Exception as error:
            print("CategorySerializer_delete_error:", error)
            return None
