import graphene
from api_graphql.schema import Query
from clinic_history.models import ClinicHistory
from django.test import TestCase

# Create your tests here.


class TestGraphModelCourier(TestCase):
    """Clase que prueba los atributos del modelo"""

    def setUp(self):
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

    def test_get_all_clinic_histories(self):
        """Prueba la consulta para obtener todos los registros"""

        schema = graphene.Schema(query=Query)
        query = """
            query {
                allClinicsHistories {
                    edges {
                        node {
                            data
                        }
                    }
                }
            }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allClinicsHistories": {
                    "edges": [
                        {
                            "node": {
                                "data": {
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
                            }
                        }
                    ]
                }
            },
            result.data,
        )
