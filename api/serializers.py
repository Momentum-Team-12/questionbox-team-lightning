from rest_framework import serializers 
from .models import Answer, Question, MyList, User


class AnswerSerializer(serializers.ModelSerializer):
    responder = serializers.SlugRelatedField(read_only=True, slug_field='username')
    question  = serializers.SlugRelatedField(read_only=True, slug_field='title')
    
    class Meta:
        model = Answer
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    creator        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    total_answers  = serializers.IntegerField(read_only=True,)
    answers     = serializers.PrimaryKeyRelatedField(many=True, read_only =True)
    class Meta:
        model  = Question
        fields = ['id','title','body','creator','created_at','answers','total_answers','modified_on','favorite_count']


class MyListSerializer(serializers.ModelSerializer):
    user     = serializers.SlugRelatedField(read_only=True,slug_field="username")
    question = serializers.SlugRelatedField(read_only =True, slug_field="title")

    
    class Meta:
        model   = MyList
        fields  = ['user','question']




        

        
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')