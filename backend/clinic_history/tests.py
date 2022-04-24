from django.db import IntegrityError
from django.test import TestCase

from .models import ClinicHistory

# Create your tests here.


class ReviewTest(TestCase):
    """Clase que prueba los atributos del modelo"""

    def setUp(self) -> None:
        """Funcion que ejecuta la configuración inicial"""

        data = {
            "userData": {
                "name": "hackathon",
                "lastname": "yeapp",
                "identificationType": "1",
                "identificationNumber": "123456789",
                "address": "manza siempre viva",
                "genre": "1"
            },
            "consultData": {
                "description": "broquitis aguda, resfriado común",
                "actualSicks": "infección de oido",
                "past": "sinusitis"
            }
        }
        ClinicHistory.objects.create(data=data)

    def test_successful_register(self) -> None:
        """Prueba la creación de un registro exitoso"""

        clinic_history = ClinicHistory.objects.first()
        self.assertTrue(clinic_history, True)
    
    def test_error_register(self) -> None:
        """Prueba la integridad del modelo"""

        with self.assertRaises(IntegrityError):
            ClinicHistory.objects.create()
