# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from demo import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['tags', 'category']
    list_display = ['text', 'category', 'posted']


admin.site.register(models.Category)
admin.site.register(models.Tag)
