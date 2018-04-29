from django.test import TestCase
from demo import models


class CategoryTests(TestCase):
    def setUp(self):
        for i in range(10):
            category = models.Category()
            category.title = 'cat{}'.format(i)
            category.save()

    def test_count(self):
        count = models.Category.objects.count()
        self.assertEqual(count, 10)
