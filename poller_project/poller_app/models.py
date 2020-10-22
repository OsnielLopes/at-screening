from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.ManyToManyField(User)