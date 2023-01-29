from strawberry.types import Info
import strawberry_django_jwt.mutations as jwt_mutations
from strawberry_django_jwt.decorators import login_required as lr
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from typing import List, Type, cast, Union, Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from strawberry_django_plus import gql
from strawberry_django_plus.permissions import IsAuthenticated
from strawberry_django_plus.types import OperationInfo

from .base import (
    uuid_update_mutation,
    uuid_delete_mutation,
    django_field,
    field,
    id_update_mutation,
    id_delete_mutation,
)
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
    user: UserType = django_field()
    users: List[UserType] = django_field()

    @field()
    def info(self, info: Info) -> InfoType:
        return InfoType(
            user=cast(UserType, info.context.request.user),
        )


@gql.type
class TeamQuery:
    team_sections: List[TeamSectionType] = django_field()


@gql.type
class PersonsQuery:
    person: PersonType = django_field(description="Retrieve Person by their id")
    # person: Optional[PersonType] = django_field(description="Person?")
    persons: List[PersonType] = django_field()
    # persons: Optional[List[PersonType]] = django_field()
    # persons: Union[List[PersonType], OperationInfo] = django_field()


@gql.type
class PersonsMutation:
    create_person: PersonType = gql.django.create_mutation(PersonInput)

    update_person: PersonType = id_update_mutation(
        PersonInputPartial,
        directives=[IsAuthenticated()],
    )
    # update_person: PersonType = gql.django.update_mutation(PersonInputPartial)
    # update_person: PersonType = update_mutation(PersonInputPartial)
    # update_person: PersonType = uuid_update_mutation(PersonInputPartial)

    delete_person: PersonType = id_delete_mutation(
        directives=[IsAuthenticated()],
    )
    # delete_person: PersonType = uuid_delete_mutation()
    # delete_person: PersonType = gql.django.delete_mutation(gql.NodeType)


@gql.type
class AuthMutation:
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie


@gql.type
class Query(
    CoreQuery,
    PersonsQuery,
    TeamQuery,
):
    ...


@gql.type
class Mutation(
    AuthMutation,
    PersonsMutation,
):
    ...


schema = gql.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        SchemaDirectiveExtension,
        DjangoOptimizerExtension,
        JSONWebTokenMiddleware,
    ],
)
