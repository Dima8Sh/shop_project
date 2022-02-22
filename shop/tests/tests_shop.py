from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from core.base_test import BaseAPITestCase
from shop.tests.factories import CategoryFactory
from shop.models import Category

class TestCategoriesApi(BaseAPITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category1 = CategoryFactory()
        cls.category2 = CategoryFactory()

        cls.admin = cls.create_user(email='admin@gamil.com', password='1234567qwe', is_staff=True)


    def test_get_category_list_success(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_category_without_permissions(self):
        url = reverse('category-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_category_by_admin_success(self):
        self.assertEqual(Category.objects.all().count(),2)
        url = reverse('category-detail', args=[self.category1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.all().count(), 1)


