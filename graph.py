
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User
from graphene import ObjectType,List, Schema

class UserGraph(SQLAlchemyObjectType):

    class Meta:
        model = User

        only_fields = ("name",)



class Query(ObjectType):

    users = List(UserGraph)

    def resolve_users(self,info):
        query = UserGraph.get_query(info)
        return query.all()


schema = Schema(query=Query)