from django.db import models
from django.utils.text import slugify
from django_lifecycle import LifecycleModelMixin, hook, BEFORE_SAVE
from mptt.models import MPTTModel,TreeForeignKey


class Category(LifecycleModelMixin, MPTTModel,models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    count_products = models.IntegerField(null=True, default=0, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    class MPTTMeta:
        order_insertion_by = ['name']


    @hook(BEFORE_SAVE)
    def set_slug(self):
        self.slug = slugify(self.name)


class Brand(LifecycleModelMixin,models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    count_products = models.IntegerField(null=True, default=0, blank=True)

    @hook(BEFORE_SAVE)
    def set_slug(self):
        self.slug = slugify(self.name)

class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    category = models.ManyToManyField(Category, related_name='category_product')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_product')
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()





