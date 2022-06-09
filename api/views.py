from api.models import MyList, Question, Answer, MyList, User
from api.serializers import MyListSerializer, QuestionSerializer,AnswerSerializer, UserSerializer,QuestionDetailSerializer,AnswerAcceptSerialize
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import  ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, get_object_or_404
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsResponderOrReadOnly, IsCreatorOrReadOnly

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.db.models import Count
from rest_framework.views import APIView

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
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["question_pk"])

    def perform_create(self, serializer, **kwargs):
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        serializer.save(responder=self.request.user, question=question)

    # @action(detail=False)
    # def accepted(self, request):
    #     accepted_answer = Answer.objects.filter(accepted=True)
    #     serializer = self.get_serializer(accepted_answer, many=True)
    #     return Response(serializer.data)

    # def get_queryset(self):
    #     search_term = self.request.query_params.get("search")
    #     if search_term is not None:
    #         results = Answer.objects.filter(response__icontains=self.request.query_params.get("search"))
    #     else:
    #         results = Answer.objects.annotate(
    #             total_answers=Count('response')
    #         )
    #     return results



class AnswerDetailEditView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsResponderOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class AnswerAcceptView(RetrieveUpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerAcceptSerializer
    permission_classes = [IsCreatorOrReadOnly]

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs["question_pk"], id=self.kwargs["pk"])

# # CDRF?
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)


class UserAnswerListView(ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(responder_id=self.kwargs["responder_pk"])


class UserQuestionListView(ListAPIView): 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(creator_id=self.kwargs["creator_pk"])


class CreateFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        
        user     = self.request.user
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        user.favorite_questions.add(question)
        serializer = QuestionDetailSerializer(QuestionDetailSerializer, context={"request": request})
        return Response(serializer.data, status=201)



class MyListView(ModelViewSet):
    queryset          = MyList.objects.all()
    serializer_class  = MyListSerializer
    permission_classes = [IsUserOrReadOnly]

    def get_queryset(self):
        return MyList.objects.filter(user_id=self.kwargs["user_pk"])

    def perform_destroy(self, instance):
        if self.request.user  == instance.user:
            instance.delete()

    def perform_update(self,serializer):
        if self.request.user == serializer.instance.user:
            serializer.save()


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)



class UserViewSet(ModelViewSet):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer

