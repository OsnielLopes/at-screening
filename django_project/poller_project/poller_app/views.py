from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from .models import Question, Answer
from .admin import site
from .forms import AnswerForm


class QuestionsToAnswer(ListView):
    model = Question

    def get_queryset(self):
        qs = super().get_queryset()
        answered_questions = Answer.objects.filter(user=self.request.user).values_list('question_id')
        qs = qs.exclude(user=self.request.user).exclude(id__in=answered_questions)
        return qs

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update(site.each_context(self.request))
        return context


class AnswerView(CreateView):
    model = Answer
    form_class = AnswerForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['question_id'] = self.kwargs['question_id']
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def get(self, request, *args, **kwargs):
        try:
            Answer.objects.get(user=request.user, question=int(kwargs['question_id']))
            return redirect('/')
        except Answer.DoesNotExist:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update(site.each_context(self.request))
        return context

    def get_success_url(self):
        return reverse('questions_to_answer')
