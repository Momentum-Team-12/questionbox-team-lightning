from api.models import Question, Answer, Favorite
from api.serializers import QuestionFavoriteSerializer, QuestionSerializer,AnswerSerializer,QuestionFavoriteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import SAFE_METHODS, BasePermission
from .permissions import IsResponderOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count


# # Create your views here.

class QuestionViewSet(ModelViewSet):
    queryset          = Question.objects.all()
    serializer_class  = QuestionSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Question.objects.filter(title__icontains=self.request.query_params.get("search"))
        else:
            results = Question.objects.annotate(
                total_answers=Count('answers')
            )
        return results

    def perform_destroy(self, instance):
        if self.request.user  == instance.creator:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.creator:
            serializer.save()
            

    
# I want to empliment a way to search the list of answers for a specific answer query. Joey_notes
# Can I follow the logic that was used to empliment the search query for QuestionViewSet? Joey_notes
#   


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
        accepted_answer = Answer.objects.filter(accepted=True)
        serializer = self.get_serializer(accepted_answer, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        search_term = self.request.query_params.get("search")
        if search_term is not None:
            results = Answer.objects.filter(response__icontains=self.request.query_params.get("search"))
        else:
            results = Answer.objects.annotate(
                total_answers=Count('response')
            )
        return results
class UserAnswerListView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(responder_id=self.kwargs["responder_pk"])
    


class AnswerDetailEditView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsResponderOrReadOnly]

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["question_pk"], answer_id=self.kwargs["answer_pk"])

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



class UserQuestionListView(ListAPIView): 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(creator_id=self.kwargs["creator_pk"])


class UserFavoriteListView(ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = QuestionFavoriteSerializer
    
    def get_queryset(self):
        return Favorite.objects.filter(user_id=self.kwargs["user_pk"])




