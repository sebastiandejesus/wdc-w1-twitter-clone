from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout as django_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .models import Tweet
from .forms import TweetForm


@login_required()
def logout(request):
    # HINT: Logout user (you can use logout() function from Django)
    # and redirect to root url
    pass

def home(request, username=None):
    # HINT: Redirect to /login url if user is not authenticated
    # and username wasn't given
    # === CODE HERE ===
    #
    # =================

    # HINT 2: Modify code below to have following behavior:
    # - If request's method is 'GET', show user's feed as before
    #   (you may send TweetForm instance as template context)
    # - If request's method is 'POST', create a Tweet for proper user, using TweetForm
    user = get_object_or_404(get_user_model(), username=username)
    tweets = Tweet.objects.filter(user=user)
    return render(request, 'feed.html', {
        'twitter_profile': user,
        'tweets': tweets
    })


@login_required()
def delete_tweet(request, tweet_id):
    # HINT: Get Tweet based on given tweet_id and delete it
    # (only if it belongs to authenticated user)
    pass
