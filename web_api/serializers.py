from rest_framework import serializers
from products.models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fiels = ['name', 'slug']


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category',
                  'name',
                  'slug',
                  'image',
                  'description',
                  'price',
                  'created']