from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import QuestionsToAnswer, AnswerView

urlpatterns = [
    path('questions-to-answer/', login_required(QuestionsToAnswer.as_view()), name='questions_to_answer'),
    path('new-answer/<question_id>/', login_required(AnswerView.as_view()))
]