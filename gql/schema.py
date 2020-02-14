import graphene
import graphql_jwt

from gql.apps.gql import schema as gql_schema


class JWTMutation(object):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(gql_schema.Query, graphene.ObjectType):
    pass


class Mutation(gql_schema.Mutation, JWTMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
