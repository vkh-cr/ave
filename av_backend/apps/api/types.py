from datetime import datetime
from typing import Type, cast, List, Optional
from uuid import UUID

from django.db import models as m
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from strawberry_django_plus import gql

from apps.api.base import IDInput
from apps.people.models import Person, TeamSection

UserModel = cast(Type[AbstractUser], get_user_model())


@gql.type
class InfoType:
    user: Optional["UserType"]


@gql.django.type(UserModel)
class UserType:
    id: gql.auto
    username: gql.auto
    email: gql.auto
    is_active: gql.auto
    is_superuser: gql.auto
    is_staff: gql.auto
    first_name: gql.auto
    last_name: gql.auto

    # TODO: what is this used for?
    # id_attr = "username"

    @gql.django.field(only=["first_name", "last_name"])
    def full_name(self, root: AbstractUser) -> str:
        return f"{root.first_name or ''} {root.last_name or ''}".strip()


@gql.django.order(TeamSection)
class TeamSectionOrder:
    code: gql.auto
    name: gql.auto


@gql.django.type(TeamSection)
class TeamSectionType:
    uuid: UUID
    code: gql.auto
    name: gql.auto
    e_mail: gql.auto
    phone: gql.auto

    members: List["PersonType"]

    created: datetime
    modified: datetime

    # TODO: what is this for?
    id_attr = "uuid"


@gql.django.order(Person)
class PersonOrder:
    code: gql.auto
    name: gql.auto

    sections: Optional[TeamSectionOrder]


@gql.django.filter(Person, lookups=True)
class PersonFilter:
    code: gql.auto
    name: gql.auto
    search: Optional[str]

    def filter_search(self, queryset: m.QuerySet[Person]):
        q = m.Q(name__icontains=self.search) | m.Q(code__icontains=self.search)
        return queryset.filter(q)


@gql.django.type(Person, order=PersonOrder, filters=PersonFilter)
class PersonType:
    id: gql.auto
    # uuid: UUID
    code: gql.auto
    name: gql.auto
    e_mail: gql.auto
    phone: gql.auto
    city: gql.auto

    sections: List[TeamSectionType]

    created: datetime
    modified: datetime

    # TODO: what is this for?
    # id_attr = "uuid"


# TODO: rename to PersonCreate
@gql.django.input(Person)
class PersonInput:
    code: gql.auto
    name: gql.auto


# TODO: rename to PersonUpdate
@gql.django.partial(Person)
class PersonInputPartial(IDInput, PersonInput):
    # code: gql.auto
    # name: gql.auto
    phone: gql.auto
