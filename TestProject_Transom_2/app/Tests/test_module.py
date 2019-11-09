from app.models.Carro import Carro
from app.models.Avion import Avion
import pytest
#pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestModels:
        def test_client(self):
            carro = Carro
            avion = Avion
            assert  carro != None 
            assert avion != None
            assert hasattr(carro, 'added')
            assert hasattr(carro, 'updated')
            assert hasattr(carro, 'color')
            assert hasattr(carro, 'modelo')
            assert hasattr(carro, 'marca')
            assert hasattr(carro, 'kilometraje')
            assert hasattr(carro, 'nuevo')
            assert hasattr(carro, 'tipo')
            assert hasattr(avion, 'added')
            assert hasattr(avion, 'updated')
            assert hasattr(avion, 'color')
            assert hasattr(avion, 'modelo')
            assert hasattr(avion, 'marca')
            assert hasattr(avion, 'kilometraje')
            assert hasattr(avion, 'nuevo')
            assert hasattr(avion, 'tipo')



           