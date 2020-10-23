from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ..poller_app.models import Question, Choice, Answer


class SignUpUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_staff = forms.BooleanField(initial=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff')

    def save(self, commit=True):
        user: User = super().save(commit)
        user.user_permissions.add(*Question.get_permissions(), *Choice.get_permissions(), *Answer.get_permissions())
        return user
