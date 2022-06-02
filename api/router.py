from api.views import QuestionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions',QuestionViewSet)