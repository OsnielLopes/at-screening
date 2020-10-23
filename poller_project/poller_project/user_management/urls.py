from django.urls import path

from poller_project.user_management.views import signup

from poller_project.user_management.views import UserProfile

urlpatterns = [
    path(r'signup/', signup, name='signup'),
    path(r'profile/<pk>', UserProfile.as_view(), name='user_profile')
]