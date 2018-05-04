# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    """
    Category model with one title field.
    """
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Tag(models.Model):
    """
    Tag model with one title field.
    """
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Post(models.Model):
    """
    Post model with Category foreign key and Tag many to many fields.
    """
    posted = models.DateTimeField(auto_now_add=True, editable=False)
    text = models.CharField(max_length=200)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('posted',)
