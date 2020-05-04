import graphene
import bajadas.schema

class Query(bajadas.schema.Query, graphene.ObjectType):
    pass
    
schema = graphene.Schema(query=Query, types=[Option, CategoryOption])