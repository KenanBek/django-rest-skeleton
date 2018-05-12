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


class TagTests(TestCase):
    def setUp(self):
        for i in range(10):
            tag = models.Tag()
            tag.title = 'tag{}'.format(i)
            tag.save()

    def test_count(self):
        count = models.Tag.objects.count()
        self.assertEqual(count, 10)


class PostTests(TestCase):
    def setUp(self):
        for i in range(10):
            post = models.Post()
            post.title = 'post{}'.format(i)
            post.save()

    def test_count(self):
        count = models.Post.objects.count()
        self.assertEqual(count, 10)
