from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer, ListQuestionSerializer
from rest_framework import ModelViewSet, status
from rest_framework.decorators import action
from rest_framework.response import Response


class QuestionViewSet(ModelViewSet):
    queryset          = Question.objects.all
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
        questions   = self.get_queryeset().filter(favorite=True)
        serializer  = self.getserializer(questions, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
