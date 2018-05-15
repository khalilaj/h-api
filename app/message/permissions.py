from rest_framework import permissions


class MessageAccessPermission(permissions.BasePermission):
    message = 'User not allowed.'

    def has_permission(self, request, view):

        account_type = request.user.user_type

        if request.method == 'GET':
            can_get = ['MN', 'TN']
            return account_type in can_get

        elif request.method == 'POST':
            can_create = ['TN']
            return account_type in can_create

        elif request.method == 'PUT':
            can_update = ['TN','MN']
            return account_type in can_update

        else:
            return False