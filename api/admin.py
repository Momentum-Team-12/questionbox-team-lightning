from django.contrib import admin
from api.models import  MyList, Question, Answer, User,MyList

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(MyList)



