from django.db import models
from .Vehiculo import Vehiculo

class Avion(Vehiculo):    
     tipo = models.CharField(max_length = 10, default="Avion")

def __init__(self):
    tipo = "Avion"