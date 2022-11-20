import dataclasses
from typing import (
    Type,
    Optional,
    Any,
    Literal,
    List,
    Union,
    Callable,
    Mapping,
    Sequence,
    Dict,
    cast,
)
from uuid import UUID

import strawberry
from django.core.exceptions import PermissionDenied
from strawberry import UNSET, BasePermission
from strawberry.django.context import StrawberryDjangoContext
from strawberry.types import Info
from strawberry_django_plus import gql
from strawberry_django_plus.mutations import resolvers
from strawberry_django_plus.mutations.fields import (
    DjangoUpdateMutationField,
    DjangoDeleteMutationField,
)
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from strawberry_django_plus.permissions import (
    running_checks,
    IsAuthenticated,
)
from strawberry_django_plus.utils.resolvers import async_safe
from strawberry_django_plus.utils.typing import UserType


def django_field(*args, **kwargs):
    directives = set(kwargs.get("directives", []))
    directives.add(IsAuthenticated())
    kwargs["directives"] = list(directives)
    return gql.django.field(*args, **kwargs)


def field(*args, **kwargs):
    directives = set(kwargs.get("directives", []))
    directives.add(IsAuthenticated())
    kwargs["directives"] = list(directives)
    return gql.field(*args, **kwargs)


@strawberry.input(
    description="UUID input",
)
class UUIDInput:
    uuid: UUID


@strawberry.input(
    description="ID input",
)
class IDInput:
    # this needs to be explicit type,
    # not gql.auto since it resolves to GlobalID
    id: int


def get_with_perms(lookups, info, *, required=False, model=None):
    try:
        instance = model.objects.filter(**lookups).get()
    except model.DoesNotExist:
        raise

    checks = running_checks.get()
    if not checks:
        return instance

    user = cast(StrawberryDjangoContext, info.context).request.user
    for check in checks:
        f = any if check.any else all
        checker = check.obj_perm_checker(info, cast(UserType, user))
        if not f(checker(p, instance) for p in check.permissions):
            raise PermissionDenied(check.message)

    return instance


def id_update_mutation(
    input_type: Type[IDInput],
    *,
    name: Optional[str] = None,
    field_name: Optional[str] = None,
    filters: Any = UNSET,
    is_subscription: bool = False,
    description: Optional[str] = None,
    init: Literal[True] = True,
    permission_classes: Optional[List[Type[BasePermission]]] = None,
    deprecation_reason: Optional[str] = None,
    default: Any = dataclasses.MISSING,
    default_factory: Union[Callable[..., object], object] = dataclasses.MISSING,
    metadata: Optional[Mapping[Any, Any]] = None,
    directives: Optional[Sequence[object]] = (),
    handle_django_errors: bool = True,
) -> Any:
    return DjangoUpdateMutationField(
        input_type=input_type,
        python_name=None,
        django_name=field_name,
        graphql_name=name,
        type_annotation=None,
        description=description,
        is_subscription=is_subscription,
        permission_classes=permission_classes or [],
        deprecation_reason=deprecation_reason,
        default=default,
        default_factory=default_factory,
        metadata=metadata,
        directives=directives,
        filters=filters,
        handle_django_errors=handle_django_errors,
    )


def id_delete_mutation(
    input_type: Type[IDInput] = IDInput,
    *,
    name: Optional[str] = None,
    field_name: Optional[str] = None,
    filters: Any = UNSET,
    is_subscription: bool = False,
    description: Optional[str] = None,
    init: Literal[True] = True,
    permission_classes: Optional[List[Type[BasePermission]]] = None,
    deprecation_reason: Optional[str] = None,
    default: Any = dataclasses.MISSING,
    default_factory: Union[Callable[..., object], object] = dataclasses.MISSING,
    metadata: Optional[Mapping[Any, Any]] = None,
    directives: Optional[Sequence[object]] = (),
    handle_django_errors: bool = True,
) -> Any:
    return DjangoDeleteMutationField(
        input_type=input_type,
        python_name=None,
        django_name=field_name,
        graphql_name=name,
        type_annotation=None,
        description=description,
        is_subscription=is_subscription,
        permission_classes=permission_classes or [],
        deprecation_reason=deprecation_reason,
        default=default,
        default_factory=default_factory,
        metadata=metadata,
        directives=directives,
        filters=filters,
        handle_django_errors=handle_django_errors,
    )


def uuid_update_mutation(
    input_type: Type[UUIDInput],
    *,
    name: Optional[str] = None,
    field_name: Optional[str] = None,
    filters: Any = UNSET,
    is_subscription: bool = False,
    description: Optional[str] = None,
    init: Literal[True] = True,
    permission_classes: Optional[List[Type[BasePermission]]] = None,
    deprecation_reason: Optional[str] = None,
    default: Any = dataclasses.MISSING,
    default_factory: Union[Callable[..., object], object] = dataclasses.MISSING,
    metadata: Optional[Mapping[Any, Any]] = None,
    directives: Optional[Sequence[object]] = (),
    handle_django_errors: bool = True,
) -> Any:
    return UUIDUpdateMutationField(
        input_type=input_type,
        python_name=None,
        django_name=field_name,
        graphql_name=name,
        type_annotation=None,
        description=description,
        is_subscription=is_subscription,
        permission_classes=permission_classes or [],
        deprecation_reason=deprecation_reason,
        default=default,
        default_factory=default_factory,
        metadata=metadata,
        directives=directives,
        filters=filters,
        handle_django_errors=handle_django_errors,
    )


class UUIDUpdateMutationField(DjangoUpdateMutationField):
    @async_safe
    def resolver(
        self,
        source: Any,
        info: Info,
        data: UUIDInput,
        args: List[Any],
        kwargs: Dict[str, Any],
    ) -> Any:
        assert data is not None

        vdata = vars(data)
        uuid = vdata.pop("uuid")

        # Do not optimize anything while retrieving the object to update
        token = DjangoOptimizerExtension.enabled.set(False)
        try:
            instance = get_with_perms(uuid, info, required=True, model=self.model)
            return resolvers.update(info, instance, resolvers.parse_input(info, vdata))
        finally:
            DjangoOptimizerExtension.enabled.reset(token)


def uuid_delete_mutation(
    input_type: Type[UUIDInput] = UUIDInput,
    *,
    name: Optional[str] = None,
    field_name: Optional[str] = None,
    filters: Any = UNSET,
    is_subscription: bool = False,
    description: Optional[str] = None,
    init: Literal[True] = True,
    permission_classes: Optional[List[Type[BasePermission]]] = None,
    deprecation_reason: Optional[str] = None,
    default: Any = dataclasses.MISSING,
    default_factory: Union[Callable[..., object], object] = dataclasses.MISSING,
    metadata: Optional[Mapping[Any, Any]] = None,
    directives: Optional[Sequence[object]] = (),
    handle_django_errors: bool = True,
) -> Any:
    return UUIDDeleteMutationField(
        input_type=input_type,
        python_name=None,
        django_name=field_name,
        graphql_name=name,
        type_annotation=None,
        description=description,
        is_subscription=is_subscription,
        permission_classes=permission_classes or [],
        deprecation_reason=deprecation_reason,
        default=default,
        default_factory=default_factory,
        metadata=metadata,
        directives=directives,
        filters=filters,
        handle_django_errors=handle_django_errors,
    )


class UUIDDeleteMutationField(DjangoDeleteMutationField):
    @async_safe
    def resolver(
        self,
        source: Any,
        info: Info,
        data: UUIDInput,
        args: List[Any],
        kwargs: Dict[str, Any],
    ) -> Any:
        assert data is not None

        vdata = vars(data)
        uuid = vdata.pop("uuid")

        # Do not optimize anything while retrieving the object to delete
        token = DjangoOptimizerExtension.enabled.set(False)
        try:
            instance = get_with_perms(uuid, info, required=True, model=self.model)
            return resolvers.delete(
                info, instance, data=resolvers.parse_input(info, vdata)
            )
        finally:
            DjangoOptimizerExtension.enabled.reset(token)
