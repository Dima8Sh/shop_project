
from rest_framework import viewsets
from .models import Brand, Category, Product
from shop import serializers as serializers_shop


class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.filter().prefetch_related()
    serializer_class = serializers_shop.BrandsSerializer


class CategoryViesViewSet(viewsets.ViewSet):
    queryset = Category.objects.filter().prefetch_related()
    serializer_class = serializers_shop.CategoriesSerializer


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.filter().prefetch_related()
    serializer_class = serializers_shop.ProductsSerializer


