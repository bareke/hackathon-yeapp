from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String

# Create your inputs types here.


class CreateClinicHistoryInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de la historia clinica
    """

    data = String(required=True)


class UpdateClinicHistoryInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de la historia clinica
    """

    id = ID(required=True)
    data = String(required=True)
