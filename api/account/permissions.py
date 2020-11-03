from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


# class BasePermission(metaclass=BasePermissionMetaclass):
#     """
#     A base class from which all permission classes should inherit.
#     """
#
#     def has_permission(self, request, view):
#         """
#         для url, к ведёт к list ( not id needed)
#         """
#         return True
#
#     def has_object_permission(self, request, view, obj):
#         """
#         для url, в которых есть id( detail/delete/update);
#         see obj in params
#         """
#         return True

class IsOwnerOrIsStaffOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view,obj):
        """over-write super method (mix existed method has_object_permission + obj in params
        adding check if obj.user is the request user
        """
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.user == request.user or request.user.is_staff)
        )