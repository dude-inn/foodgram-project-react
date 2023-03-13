from rest_framework.permissions import (BasePermission,
                                        IsAuthenticatedOrReadOnly)


class AuthorAdminOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    Автору и админу разрешено всё, остальным только чтение.
    Если не автор, то владелец учетки
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET',):
            return True
        if request.user == obj.author:
            return request.user.is_authenticated
        return (
            request.user.is_authenticated
            and (
                request.user.is_superuser
                or request.user == obj
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
