from typing import Sequence, Type, TYPE_CHECKING

from importlib import import_module

from django.conf import settings

from django.contrib import auth

from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BaseAuthentication

from rest_framework_simplejwt.authentication import JWTAuthentication 


def get_auth_header(headers):
    value = headers.get('Authorization')

    if not value:
        return None

    auth_type, auth_value = value.split()[:2]

    return auth_type, auth_value


if TYPE_CHECKING:
    # This is going to be resolved in the stub library
    # https://github.com/typeddjango/djangorestframework-stubs/
    from rest_framework.permissions import _PermissionClass

    PermissionClassesType = Sequence[_PermissionClass]
else:
    PermissionClassesType = Sequence[Type[BasePermission]]


class ApiAuthMixin:
    authentication_classes: Sequence[Type[BaseAuthentication]] = [
            JWTAuthentication,
    ]
    permission_classes: PermissionClassesType = (IsAuthenticated, )
