# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Buildings.models import Models, Sensors, Holes, Demo

@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ('id','modelName','latitude', 'longitude', 'height', 'description')
    search_fields = ('modelName',)
@admin.register(Sensors)
class SensorsAdmin(admin.ModelAdmin):
    list_display = ('modelName', 'sensorId','latitude', 'longitude', 'height', 'internal')
    list_filter = ('modelName',)
    search_fields = ('modelName',)

# @admin.register(Demo)
# class DemoAdmin(admin.ModelAdmin):
#     list_display = ('modelName',)

@admin.register(Holes)
class HolesAdmin(admin.ModelAdmin):
    list_display = ('modelName', 'sensorId', 'east', 'south', 'west', 'north', 'maxHeight', 'minHeight', 'serialNum')
    list_filter = ('modelName','sensorId')
    search_fields = ('modelName',)
admin.site.site_header = '基坑平台数据管理系统'
admin.site.site_title = '基坑平台数据管理系统'