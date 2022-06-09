from api.views import MyListView, QuestionViewSet, UserViewSet
from rest_framework import routers
from rest_framework_nested import routers
from api import views as api_views


router = routers.DefaultRouter()
router.register('questions',api_views.QuestionViewSet)
router.register('users',api_views.UserViewSet,basename='users')
users_router = routers.NestedSimpleRouter(router,'users', lookup='user')
users_router.register(
    'mylist',
    api_views.MyListView,
    basename='my_list',
)
