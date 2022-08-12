from rest_framework.permissions import BasePermission
from authentication.utils import UserType

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == UserType.MANAGER

class IsCoManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == UserType.COMANAGER

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.type == UserType.EMPLOYEE