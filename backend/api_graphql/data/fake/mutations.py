from faker import Faker
from graphene import Int
from graphene import Boolean
from graphene import Mutation

from clinic_history.models import ClinicHistory

# Create your mutations here


class FakeData(Mutation):
    """Clase para generar datos falsos"""

    response = Boolean()

    class Arguments:
        number = Int(required=True)

    def mutate(self, info, number: Int):
        try:
            faker = Faker()
            for i in range(number):
                name, lastname = faker.name().split()
                data = {
                    "nombres": name,
                    "apellidos": lastname,
                    "tipo_documento": "cedula",
                    "numero_documento": faker.ean13(),
                    "genero": "m",
                    "telefono": faker.phone_number(),
                    "direccion": faker.address(),
                    "descripcion": faker.sentence(),
                    "enfermedades": faker.sentence(),
                    "antecedentes": faker.sentence()
                }
                ClinicHistory.objects.create(data=data)
                response = True
        except:
            response = False

        return FakeData(response=response)
