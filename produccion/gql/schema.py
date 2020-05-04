import graphene
import bajadas.schema
import users.schema

class Query(bajadas.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, bajadas.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
