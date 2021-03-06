# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Models(models.Model):
    modelName = models.CharField(max_length=20, unique=True, verbose_name='模型名')
    latitude = models.CharField(max_length=30, verbose_name='纬度')
    longitude = models.CharField(max_length=30, verbose_name='经度')
    height = models.CharField(max_length=30, verbose_name='高度')
    modelUrl = models.CharField(max_length=45, verbose_name='模型存储路径')
    scale = models.CharField(max_length=10, verbose_name='模型比例')
    description = models.CharField(max_length=50, verbose_name='描述')

    class Meta:
        verbose_name = '模型'
        verbose_name_plural = '模型'
    def __str__(self):
        return self.modelName

class Sensors(models.Model):
    # modelName = models.ForeignKey(Models, verbose_name='模型名')
    modelName = models.CharField(max_length=40, verbose_name='模型名')
    sensorId = models.IntegerField(default=0, verbose_name='传感器编号')
    latitude = models.CharField(max_length=30, verbose_name='纬度')
    longitude = models.CharField(max_length=30, verbose_name='经度')
    height = models.CharField(max_length=30, verbose_name='高度')
    holesNum = models.IntegerField(default=0, verbose_name='测孔数')
    internal = models.FloatField(default=0, verbose_name='测孔间距')

    class Meta:
        verbose_name = '传感器'
        verbose_name_plural = '传感器'
    # def __str__(self):
    #     return self.sensorId

class Holes(models.Model):
    east = models.CharField(max_length=45, verbose_name='东')
    south = models.CharField(max_length=45, verbose_name='南')
    west = models.CharField(max_length=45, verbose_name='西')
    north = models.CharField(max_length=45, verbose_name='北')
    maxHeight = models.CharField(max_length=45)
    minHeight = models.CharField(max_length=45)
    # sensorId = models.ForeignKey(Sensors, verbose_name='传感器编号')
    sensorId = models.IntegerField(default=0, verbose_name='传感器编号')
    serialNum = models.IntegerField(default=1, verbose_name='色块序号')
    # modelName = models.ForeignKey(Models, verbose_name='模型名')
    modelName = models.CharField(max_length=40, verbose_name='模型名')

    class Meta:
        verbose_name = "色块"
        verbose_name_plural = "色块"

class Demo(models.Model):
    modelName = models.ForeignKey(Models, verbose_name='模型名')