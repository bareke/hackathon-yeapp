from graphene.relay import Node
from graphene_django import DjangoObjectType
from api_graphql.connections import TotalCountConnection

from clinic_history.models import ClinicHistory

# Create your objects types here.


class ClinicHistoryNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = ClinicHistory
        filter_fields = {
            'created_at': ['exact'],
            'updated_at': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
