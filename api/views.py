from django.shortcuts import render
from api.models import Question
from api.serializers import QuestionSerializer, ListQuestionSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class QuestionViewSet(ModelViewSet):
    queryset          = Question.objects.all()
    serializer_class  = QuestionSerializer

    def get_serializer_class(self):
        if self.action in ['list',]:
            return ListQuestionSerializer
        return super().get_serializer_class()

    def perform_destroy(self, instance):
        if self.request.user  == instance.user:
            instance.delete()
    
   
