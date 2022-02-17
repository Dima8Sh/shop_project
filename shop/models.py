from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    count_products = models.IntegerField()


class Brand(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    count_products = models.IntegerField()
