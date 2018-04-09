from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError

from twitter.models import Tweet
from twitter.forms import TweetForm


@login_required
def index(request):
    context = dict()
    if request.method == 'POST':

        if 'delete_tweet' in request.POST:
            _id = request.GET.get('id', None)
            Tweet.objects.filter(id=_id).delete()
            messages.success(request, "Tweet successfully deleted")
            return redirect('index')

        form = TweetForm(request.POST)

        if form.is_valid():
            new_tweet = Tweet(username=request.user,
                              tweet=request.POST['tweet'])
            try:
                new_tweet.full_clean()
                new_tweet.save()
            except ValidationError as e:
                context['error'] = e.message_dict['tweet'][0]
            else:
                messages.success(request, "Tweet Created!")
                return redirect('index')
    else:
        form = TweetForm()

    context['form'] = form
    context['tweets'] = Tweet.objects.filter(
        username=request.user).order_by('-post_date')

    return render(request, 'authenticated_user_feed.html', context)


def show_user_tweets(request, username):
    context = {'tweets': Tweet.objects.filter(
        username=username).order_by('-post_date'),
    }
    return render(request, 'browsing_other_user_feed.html', context)
