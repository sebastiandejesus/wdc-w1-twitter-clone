from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # HINTS: Add urls for following functionalities:
    # - Login
    # - Logout
    # - Delete tweet (based on given tweet id)
    # - Root url ('/') to show authenticated user's feed
    url(r'^(?P<username>\w+)$', views.home),
]
