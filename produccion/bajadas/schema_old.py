import graphene
"""
from graphene_django.types import DjangoObjectType

from bajadas.models import bajada

class BajadaType(DjangoObjectType)
    class Meta:
        model = bajada

class Query(graphene.ObjectType)
    bajadas = graphene.List(BajadaType)

    def resolve_bajadas(self, info, *)
        return bajada.object.All()

    
"""