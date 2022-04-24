from graphene import Field
from graphene import Mutation

from clinic_history.models import ClinicHistory
from api_graphql.data.clinic_history.types import ClinicHistoryNode
from api_graphql.data.clinic_history.inputs import CreateClinicHistoryInput
from api_graphql.data.clinic_history.inputs import UpdateClinicHistoryInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

# Create your mutations here


class CreateClinicHistory(Mutation):
    """Clase para crear historias clínicas"""

    clinic_history = Field(ClinicHistoryNode)

    class Arguments:
        input = CreateClinicHistoryInput(required=True)

    def mutate(self, info, input: CreateClinicHistoryInput):
        input = delete_attributes_none(**vars(input))
        clinic_history = ClinicHistory.objects.create(**input)

        return CreateClinicHistory(clinic_history=clinic_history)


class UpdateClinicHistory(Mutation):
    """Clase para actualizar historias clínicas"""

    clinic_history = Field(ClinicHistoryNode)

    class Arguments:
        input = UpdateClinicHistoryInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos
        input = delete_attributes_none(**vars(input))
        
        # Transforma el id
        input = transform_global_ids(**input)

        ClinicHistory.objects.filter(pk=input.get('id')).update(**input)
        clinic_history = ClinicHistory.objects.get(pk=input.get('id'))

        return UpdateClinicHistory(clinic_history=clinic_history)
