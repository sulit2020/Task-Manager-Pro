import graphene
import api.schema as api_schema

class Query(api_schema.Query,graphene.ObjectType):
    pass

class Mutation(api_schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
