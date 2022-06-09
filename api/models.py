from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.username

class Question(models.Model):
    title       = models.CharField(max_length=300, null=True, blank=True)
    body        = models.TextField(null=True, blank=True)
    creator     = models.ForeignKey('User', related_name='questions', on_delete=models.CASCADE, null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User,related_name='favorite_questions', blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__ (self):
        return self.title

    def favorite_count(self):
        return self.favorited_by.count()

class Answer(models.Model):

    response    = models.TextField()
    responder   = models.ForeignKey('User', related_name='answers', on_delete=models.CASCADE, null=True,blank=True)
    question    = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE, null=True,blank=True)   
    accepted    = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    

    def __str__ (self):
        return self.response 



class MyList(models.Model):
    question    = models.ForeignKey('Question', related_name='my_lists',on_delete=models.CASCADE)
    user        = models.ForeignKey('User', related_name= 'my_lists', on_delete=models.CASCADE)

    class Meta:
            constraints  = [
                models.UniqueConstraint(fields =['question','user'], name='my_list')
            ]