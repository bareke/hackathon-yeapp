from graphene import InputObjectType
from graphene.types.generic import GenericScalar
from graphene.types.scalars import ID

# Create your inputs types here.


class CreateClinicHistoryInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de la historia clinica
    """

    data = GenericScalar(required=True)


class UpdateClinicHistoryInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de la historia clinica
    """

    id = ID(required=True)
    data = GenericScalar(required=True)
