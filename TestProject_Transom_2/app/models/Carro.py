from django.db import models
from .Vehiculo import Vehiculo

class Carro(Vehiculo):    
     tipo = models.CharField(max_length = 10, default="Carro")

def __init__(self):
    tipo = "Carro"

