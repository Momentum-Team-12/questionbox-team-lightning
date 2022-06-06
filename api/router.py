from api.views import QuestionViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('questions',QuestionViewSet)
