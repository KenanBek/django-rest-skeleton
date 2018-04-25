# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from demo import models

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Post)
