
# -*- coding: utf-8 -*-
from django.db import models

class Vehiculo(models.Model):
    """The base model"""
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    color = models.CharField(max_length = 75)
    modelo = models.CharField(max_length = 50)
    marca = models.CharField(max_length = 50)
    kilometraje = models.PositiveIntegerField(default=0)
    nuevo  = models.BooleanField(default = True)
    tipo = models.CharField(max_length = 10)

    def __str__(self):
        return self.tipo + "-" + self.marca + " " + self.modelo + " " + self.color  

    class Meta:
        abstract = True
