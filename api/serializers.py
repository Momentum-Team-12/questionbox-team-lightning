from rest_framework import serializers 
from .models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    responder = serializers.SlugRelatedField(read_only=True, slug_field='responder')
    question  = serializers.SlugRelatedField(read_only=True, slug_field='question')
    class Meta:
        model = Answer
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    creator        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    total_answers  = serializers.IntegerField()
    class Meta:
        model  = Question
        fields = ['id','name','description','creator','created_at','total_answers' ]

class ListQuestionSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model  = Question
        fields = ['id','name','creator','name','description','created_at']



        
