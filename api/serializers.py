from rest_framework import serializers
from models import Question

class QuestionSerializer(serializers.Serializer):
    
    class Meta:
        model  = Question
        fields = ['id','name','description','creator','created_at','favorite' ]

class ListQuestionSerializer(serializers.Serializer):
    
    class Meta:
        model  = Question
        fields = ['id','name','creator']