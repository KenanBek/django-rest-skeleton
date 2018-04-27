# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from demo import models


class TagSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Tag model.
    """

    class Meta:
        model = models.Tag
        fields = ('title',)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Category model.
    """

    class Meta:
        model = models.Category
        fields = ('title',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Post model.
    """

    class Meta:
        model = models.Post
        fields = ('posted', 'text', 'category', 'tags')
