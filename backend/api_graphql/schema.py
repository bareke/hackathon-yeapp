
from api_graphql.data.clinic_history.mutations import (
    CreateClinicHistory,
    UpdateClinicHistory
)
from api_graphql.data.clinic_history.types import ClinicHistoryNode
from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from api_graphql.data.fake.mutations import FakeData

# Schema definition


class Query(ObjectType):
    """Endpoint para consultar registros"""

    clinic_history = Node.Field(ClinicHistoryNode)
    all_clinics_histories = DjangoFilterConnectionField(ClinicHistoryNode)


class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""

    create_clinic_history = CreateClinicHistory.Field(description='Crear historia clínica')
    update_clinic_history = UpdateClinicHistory.Field(description='Actualizar historia clínica')
    create_fake_data = FakeData.Field(description='Generar datos falsos')
