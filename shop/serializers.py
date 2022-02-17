from rest_framework import serializers

from .models import Brand, Category, Product


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        field = ["name"]


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        field = ["name"]


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ["name"]