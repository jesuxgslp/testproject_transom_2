from django import forms
from .models.Carro import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = [
            'color',
            'modelo',
            'marca',
            'kilometraje',
            'nuevo',
            'tipo'
        ]  
        labels = {
            'color':('Color:'),
            'modelo':('Modelo:'),
            'marca':('Marca:'),
            'kilometraje':('Kilometraje: '),
            'nuevo':('Nuevo:'),
            'tipo':('Tipo:')
        }
        

