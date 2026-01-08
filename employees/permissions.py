from rest_framework.permissions import BasePermission
from .models import Employee

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        emp = Employee.objects.filter(phone=request.user.username).first()
        return emp and emp.role == 'OWNER'

class IsOwnerOrManager(BasePermission):
    def has_permission(self, request, view):
        emp = Employee.objects.filter(phone=request.user.username).first()
        return emp and emp.role in ['OWNER', 'MANAGER']

class IsMember(BasePermission):
    def has_permission(self, request, view):
        emp = Employee.objects.filter(phone=request.user.username).first()
        return emp and emp.role == 'MEMBER'
