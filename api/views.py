from django.shortcuts import render
from api.serializers import AnswerSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import Answer


# Create your views here.

#permission code from viewset tutorial - https://www.youtube.com/watch?v=dCbfOZurCQk
#repository - https://github.com/veryacademy/YT-Django-DRF-Simple-Blog-Series-Viewset-Routers-Part-4/blob/master/django/blog_api/views.py
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class AnswerView(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


