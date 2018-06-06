# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Building(models.Model):
    modelName = models.CharField(max_length=20, unique=True)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    height = models.CharField(max_length=30)
    modelUrl = models.CharField(max_length=45)
    scale = models.CharField(max_length=10)
    description = models.CharField(max_length=50)