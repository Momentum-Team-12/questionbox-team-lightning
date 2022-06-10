from rest_framework import permissions


class IsResponderOrReadOnly(permissions.BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.responder == request.user:
            return True
        return False


class IsCreatorOrReadOnly(permissions.BasePermission):
    message = 'Only the question creator can accept an answer.'
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.question.creator == request.user:
            return True
        return False


class IsUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user:
            return True
        return False