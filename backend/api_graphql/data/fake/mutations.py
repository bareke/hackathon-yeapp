import logging
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
                    "userData": {
                        "name": name,
                        "lastname": lastname,
                        "identificationType": "1",
                        "identificationNumber": faker.ean13(),
                        "address": faker.address(),
                        "genre": "m"
                    },
                    "consultData": {
                        "description": "colesterol alto",
                        "actualSicks": faker.sentence(),
                        "antepastcedentes": faker.sentence()
                    }
                }
                ClinicHistory.objects.create(data=data)
                logging.info("generating fake data successfully")
                response = True
        except:
            logging.warning("error generating fake data")
            response = False

        return FakeData(response=response)
