# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Buildings.models import Models, Sensors, Demo

@admin.register(Models)
class ModelsAdmin(admin.ModelAdmin):
    list_display = ('id','modelName','latitude', 'longitude', 'height', 'description')
    search_fields = ('modelName',)
    # list_per_page = 1
@admin.register(Sensors)
class SensorsAdmin(admin.ModelAdmin):
    list_display = ('modelName', 'sensorId','latitude', 'longitude', 'height', )

@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    list_display = ('modelName',)
admin.site.site_header = '基坑平台数据管理系统'
admin.site.site_title = '基坑平台数据管理系统'
# adminSite.register(Building, BuildingAdmin)