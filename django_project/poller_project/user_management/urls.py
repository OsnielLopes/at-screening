from django.urls import path

from .views import signup, UserProfile

urlpatterns = [
    path(r'signup/', signup, name='signup'),
    path(r'profile/<pk>', UserProfile.as_view(), name='user_profile')
]