from api.views import MyListView, QuestionViewSet, UserViewSet
from rest_framework import routers
from rest_framework_nested import routers
from api import views as api_views


router = routers.DefaultRouter()
router.register('questions',QuestionViewSet)
router.register('users',UserViewSet,basename='users')
users_router = routers.NestedSimpleRouter(router,'users', lookup='user')
users_router.register(
    'mylist',
    MyListView,
    basename='my_list',
)
