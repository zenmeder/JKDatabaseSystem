# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Buildings.models import Building

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('modelName',)
    search_fields = ('modelName',)