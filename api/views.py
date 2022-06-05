from api.models import Question, Answer
from api.serializers import QuestionSerializer, ListQuestionSerializer, AnswerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count


# # Create your views here.

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

    def get_queryset(self):
        return Question.objects.annotate(
            total_answers=Count('answers'),    
        )
    


# #permission code from viewset tutorial - https://www.youtube.com/watch?v=dCbfOZurCQk
# #repository - https://github.com/veryacademy/YT-Django-DRF-Simple-Blog-Series-Viewset-Routers-Part-4/blob/master/django/blog_api/views.py
# class PostUserWritePermission(BasePermission):
#     message = 'Editing posts is restricted to the author only.'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True

#         return obj.author == request.user

# class AnswerView(viewsets.ModelViewSet):
#     serializer_class = AnswerSerializer
#     queryset = Answer.objects.all()


class AnswerListCreateView(ListCreateAPIView):
    serializer_class = AnswerSerializer
    # permission_classes = [IsResponderOrReadOnly]
    #Amy provided a custom permissions file in her api that has classes for different permissions she created, I am thinking we will need this file or atleast the class for "IsReviewerOrReadOnly"

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["question_pk"])

    def perform_create(self, serializer, **kwargs):
        question = get_object_or_404(Answer, pk=self.kwargs["question_pk"])
        serializer.save(answered_by=self.request.user, question=question)

    @action(detail=False)
    def accepted(self, request):
        accepted_answer = Answer.objects.filter(featured=True)
        serializer = self.get_serializer(accepted_answer, many=True)
        return Response(serializer.data)

class UserAnswerListView(ListAPIView):
    serializer_class=AnswerSerializer

    def get_queryset(self):
        return self.request.user.answer_user.all()
