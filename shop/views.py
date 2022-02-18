
from rest_framework import viewsets
from .models import Brand, Category, Product
from shop import serializers as serializers_shop


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers_shop.BrandsSerializer


class CategoryViesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers_shop.CategoriesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers_shop.ProductsSerializer


