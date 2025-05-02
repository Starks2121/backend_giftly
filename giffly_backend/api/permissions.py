from rest_framework.permissions import BasePermission

class IsSellerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['seller', 'admin']

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user