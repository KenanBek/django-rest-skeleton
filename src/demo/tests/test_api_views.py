from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from demo import models


class BaseAPITests(APITestCase):
    def test_api(self):
        r = self.client.get('/api/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_docs(self):
        r = self.client.get('/docs/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_schemas(self):
        r = self.client.get('/schemas/')
        self.assertEqual(r.status_code, status.HTTP_200_OK)


class CategoryAPITests(APITestCase):
    def setUp(self):
        for i in range(10):
            category = models.Category()
            category.title = 'cat{}'.format(i)
            category.save()

    def test_list(self):
        u = reverse('category-list')
        r = self.client.get(u)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_get(self):
        u = reverse('category-detail', kwargs={'pk': 1})
        r = self.client.get(u)

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data['title'], 'cat0', 'Can not properly get Category')
