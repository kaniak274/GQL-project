import graphene

from gql.apps.gql import schema as gql_schema


class Query(gql_schema.Query, graphene.ObjectType):
    pass


class Mutation(gql_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
