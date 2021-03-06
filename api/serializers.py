from rest_framework import serializers 
from .models import Answer, Question, MyList, User


class AnswerSerializer(serializers.ModelSerializer):
    responder = serializers.SlugRelatedField(read_only=True, slug_field='username')
    question  = serializers.SlugRelatedField(read_only=True, slug_field='title')
    accepted  = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Answer
        fields = ('__all__')
        

class QuestionSerializer(serializers.ModelSerializer):
    creator        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    total_answers  = serializers.IntegerField(read_only=True,)
    # answers     = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model  = Question
        fields = ['id','title','body','creator','created_at','total_answers','modified_on','favorite_count',]


class MyListSerializer(serializers.ModelSerializer):
    user     = serializers.SlugRelatedField(read_only=True,slug_field="username")
    question = serializers.SlugRelatedField(read_only =True, slug_field="title")
    
    
    class Meta:
        model   = MyList
        fields  = ['pk','user','question',]


class AnswerDetailSerializer(serializers.ModelSerializer):
    responder = serializers.SlugRelatedField(read_only=True, slug_field='username')
    question  = serializers.SlugRelatedField(read_only=True, slug_field='title')
    accepted  = serializers.BooleanField(read_only=True)

    class Meta:
        model = Answer
        fields = ('__all__')
        


class AnswerAcceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['accepted']
        read_only_fields = ['response', 'responder', 'question', 'id' ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')


class QuestionDetailSerializer(serializers.ModelSerializer):
    creator        = serializers.SlugRelatedField(read_only=True, slug_field="username")
    total_answers  = serializers.IntegerField(read_only=True,)
    class Meta:
        model  = Question
        fields = ['id','title','body','creator','created_at','total_answers','modified_on','favorite_count',]

