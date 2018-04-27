# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from demo import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ('posted', 'text')
