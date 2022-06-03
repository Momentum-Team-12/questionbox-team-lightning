from django.contrib import admin
from api.models import  Question, Answer, User

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)



