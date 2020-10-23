from django.urls import path

from django_project.user_management.views import signup

from django_project.user_management.views import UserProfile

urlpatterns = [
    path(r'signup/', signup, name='signup'),
    path(r'profile/<pk>', UserProfile.as_view(), name='user_profile')
]