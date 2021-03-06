"""questionbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.router import router, users_router
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
    path(
        "api/questions/<int:question_pk>/answers",
        api_views.AnswerListCreateView.as_view(),
        name="question_answers",
    ),
    path("api/questions/<int:question_pk>/answers/<int:pk>", api_views.AnswerDetailEditView.as_view(), name="answer_edit"),
    path("api/questions/<int:question_pk>/answers/<int:pk>/accept", api_views.AnswerAcceptView.as_view(), name="accept_answer"),
    path('api/user/<int:creator_pk>/questions', api_views.UserQuestionListView.as_view(), name="user_questions"),
    path('api/user/<int:responder_pk>/answers', api_views.UserAnswerListView.as_view(), name="user_answers"),
    path('api/questions/<int:question_pk>/favorites', api_views.CreateFavoriteView.as_view(), name ="create_favorites"),
]

