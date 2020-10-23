from django import forms
from django.contrib.auth.models import User

from .models import Question, Choice, Answer


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(Question.objects.all(), required=True, widget=forms.HiddenInput())
    choice = forms.ModelChoiceField(Choice.objects.all(), required=True)
    user = forms.ModelChoiceField(User.objects.all(), widget=forms.HiddenInput(), required=True)
    question_text = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        question_id = int(kwargs.pop('question_id'))
        user_id = kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        self.fields['question'].initial = question_id
        self.fields['user'].initial = user_id
        question_text = Question.objects.get(id=question_id).question_text
        self.fields['question_text'].initial = question_text
        self.fields['question_text'].widget.attrs['disabled'] = True
        self.fields['question_text'].widget.attrs['size'] = len(question_text)*1.5
        self.fields['choice'].queryset = Choice.objects.filter(question_id=question_id)

    class Meta:
        model = Answer
        fields = ('question_text', 'question', 'choice', 'user')
