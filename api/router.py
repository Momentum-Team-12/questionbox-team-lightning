from api.views import AnswerView
from rest_framework import routers


router = routers.DefaultRouter()

router.register('answer', AnswerView)