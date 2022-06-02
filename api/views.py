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
        if self.action in ['list','favorite']:
            return ListQuestionSerializer
        return super().get_serializer_class()

    def perform_destroy(self, instance):
        if self.request.user  == instance.user:
            instance.delete()
    
    @action(detail=False, methods=["get"])
    def favorite(self,request):
        questions   = self.get_queryset().filter(favorite=True)
        serializer  = self.get_serializer(questions, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
