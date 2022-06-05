from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Question(models.Model):
    name        = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    creator     = models.ForeignKey('User', related_name='questions', on_delete=models.CASCADE, null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    favorite    = models.ForeignKey('Favorite', related_name='questions', on_delete=models.CASCADE, null=True,blank=True)

    def __str__ (self):
        return self.name


class Answer(models.Model):
    response   = models.TextField()
    responder  = models.ForeignKey('User', related_name='responders', on_delete=models.CASCADE, null=True,blank=True)
    question   = models.ForeignKey('Question', related_name='questions', on_delete=models.CASCADE, null=True,blank=True)
    accepted   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__ (self):
        return self.response 



class Accepted(models.Model):
    response    = models.ForeignKey('Answer', related_name='accepteds',on_delete=models.CASCADE)
    user        = models.ForeignKey('User', related_name= 'accepteds', on_delete=models.CASCADE)



class Favorite(models.Model):
    question    = models.ForeignKey('Question', related_name='favorites',on_delete=models.CASCADE)
    user        = models.ForeignKey('User', related_name= 'favorites', on_delete=models.CASCADE)