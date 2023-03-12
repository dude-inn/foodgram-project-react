from rest_framework.permissions import (BasePermission,
                                        IsAuthenticatedOrReadOnly)


class AuthorAdminOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    Автору, владельцу учётки и администраторам разрешено всё,
    остальным только чтение.
    """

    def has_object_permission(self, request, view, obj):
        if obj.author:
            return (
                request.method in ('GET',)
                or (
                    request.user.is_authenticated
                    and (
                        request.user.is_superuser
                        or request.user == obj.author
                    )
                )
            )
        return (
            request.method in ('GET',)
            or (
                request.user.is_authenticated
                and (
                    request.user.is_superuser
                    or request.user == obj
                )
            )
        )


class AdminOrReadOnly(BasePermission):
    """Админу можно всё, остальным только чтение."""

    def has_permission(self, request, view):
        return (
            request.method in ('GET',)
            or (
                request.user.is_authenticated
                and request.user.is_superuser
            )
        )
