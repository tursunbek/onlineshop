from django.shortcuts import render

from products.models import Category, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CategoryListSerializer, ProductListSerializer


class CategoryListView(APIView):
    def __get__(self, request, category_slug=None):
        categories = Category.objects.all()
        products = Product.objects.fielter(status=True)
        category_serializer = CategoryListSerializer(categories, many=True)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(category=category)
        product_serializer = ProductListSerializer(products, many=True)
        response_data = {
            'products': product_serializer.data,
            'categories': category_serializer.data
        }
        return Response(response_data)

