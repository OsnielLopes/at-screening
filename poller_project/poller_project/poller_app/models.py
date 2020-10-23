from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


class PollerBaseModel(models.Model):
    @classmethod
    def get_permissions(cls):
        content_type = ContentType.objects.get_for_model(cls)
        return list(Permission.objects.filter(content_type=content_type))

    class Meta:
        abstract = True


class Question(PollerBaseModel):
    question_text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(PollerBaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(PollerBaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
