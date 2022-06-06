from rest_framework import serializers 
from .models import Answer, Question, Favorite


class AnswerSerializer(serializers.ModelSerializer):
    responder = serializers.SlugRelatedField(read_only=True, slug_field='username')
    question  = serializers.SlugRelatedField(read_only=True, slug_field='title')
    
    class Meta:
        model = Answer
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    creator        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    total_answers  = serializers.IntegerField(read_only=True,)
    answers        = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())
   

    class Meta:
        model  = Question
        fields = ['id','title','body','creator','created_at','answers','total_answers' ]


class QuestionFavoriteSerializer(serializers.ModelSerializer):
    user     = serializers.SlugRelatedField(read_only=True,slug_field="username")
    question = serializers.SlugRelatedField(read_only =True, slug_field="title")

    
    class Meta:
        model   = Favorite
        fields  = ['user','question']
        
