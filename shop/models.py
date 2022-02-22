from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    count_products = models.IntegerField(null=True, default=0, blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    count_products = models.IntegerField(null=True, default=0, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ManyToManyField(Category, related_name='category_product')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_product')
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()





