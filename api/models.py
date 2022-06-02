from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField


class User(AbstractUser):
   
    def __str__(self):
        return self.username

class Question(models.Model):
    name        = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    creator     = models.ForeignKey('User', related_name='questions', on_delete=models.CASCADE, null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name


class Answer(models.Model):
    response   = models.TextField(null=True, blank=True)
    responder  = models.ForeignKey('User', related_name='answers', on_delete=models.CASCADE, null=True,blank=True)
    question   = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorite   = models.BooleanField(default=False)



class Accepted(models.Model):
    response    = models.ForeignKey('Answer', related_name='accepteds',on_delete=models.CASCADE)
    user        = models.ForeignKey('User', related_name= 'accepteds', on_delete=models.CASCADE)



class Favorite(models.Model):
    question    = models.ForeignKey('Question', related_name='favorites',on_delete=models.CASCADE)
    user        = models.ForeignKey('User', related_name= 'favorites', on_delete=models.CASCADE)