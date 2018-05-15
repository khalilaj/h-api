from rest_framework import permissions


class ManagerAccessPermission(permissions.BasePermission):
    message = 'User not allowed.'

    def has_permission(self, request, view):

        account_type = request.user.user_type

        if request.method == 'GET':
            can_get = ['AD']
            return account_type in can_get

        elif request.method == 'POST':
            can_create = ['AD']
            return account_type in can_create

        elif request.method == 'PUT':
            can_update = ['MN']
            return account_type in can_update

        elif request.method == 'DELETE':
            can_delete = ['AD']
            return account_type in can_delete
        else:
            return False