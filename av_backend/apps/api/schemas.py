from strawberry.types import Info
import strawberry_django_jwt.mutations as jwt_mutations
from strawberry_django_jwt.decorators import login_required as lr
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from typing import List, Type, cast

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from strawberry_django_plus import gql
from strawberry_django_plus.permissions import IsAuthenticated

from .base import update_mutation, delete_mutation
from .types import (
    UserType,
    TeamSectionType,
    PersonType,
    InfoType,
    PersonInputPartial,
    PersonInput,
)

UserModel = cast(Type[AbstractUser], get_user_model())


@gql.type
class CoreQuery:
    users: List[UserType] = gql.django.field()

    @gql.field(directives=[IsAuthenticated()])
    def info(self, info: Info) -> InfoType:
        user = None
        if info.context.request.user.pk:
            user = UserModel.objects.get(pk=info.context.request.user.pk)

        return InfoType(
            user=user,
        )


@gql.type
class TeamQuery:
    team_sections: List[TeamSectionType] = gql.django.field(
        directives=[IsAuthenticated()]
    )


@gql.type
class PersonsQuery:
    # persons: List[PersonType] = lr(gql.django.field(directives=[IsAuthenticated()]))
    persons: List[PersonType] = gql.django.field(directives=[IsAuthenticated()])


@gql.type
class PersonsMutation:
    create_person: PersonType = gql.django.create_mutation(PersonInput)
    update_person: PersonType = update_mutation(PersonInputPartial)
    delete_person: PersonType = delete_mutation()
    # update_person: PersonType = gql.django.update_mutation(PersonInputPartial)
    # delete_person: PersonType = gql.django.delete_mutation(gql.NodeType)


@gql.type
class Query(PersonsQuery, TeamQuery, CoreQuery):
    ...


@gql.type
class Mutation(PersonsMutation):
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie


schema = gql.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        SchemaDirectiveExtension,
        DjangoOptimizerExtension,
        JSONWebTokenMiddleware,
    ],
)
