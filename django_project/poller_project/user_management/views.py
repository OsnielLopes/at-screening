from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from django_project.user_management.forms import SignUpUserForm

from django_project.poller_app.admin import site


def signup(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpUserForm()
    return render(request, 'signup.html', {'form': form})


class UserProfile(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'username', 'email')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update(site.each_context(self.request))
        return context

    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.id})
