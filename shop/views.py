
from rest_framework import viewsets
from .models import Brand, Category, Product
from shop import serializers as serializers_shop
from .permissions import ProductPermissions, BrandPermissions, CategoryPermissions


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = serializers_shop.BrandsSerializer
    permission_classes = [BrandPermissions]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers_shop.CategoriesSerializer
    permission_classes = [CategoryPermissions]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers_shop.ProductsSerializer
    permission_classes = [ProductPermissions]


