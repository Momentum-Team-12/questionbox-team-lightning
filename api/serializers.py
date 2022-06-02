from rest_framework import serializers
from api.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Question
        fields = ['id','name','description','creator','created_at', ]

class ListQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Question
        fields = ['id','name','creator', 'description','created_at']



        #use slug related field