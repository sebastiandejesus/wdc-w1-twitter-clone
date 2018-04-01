import pytest

from twitter.models import Tweet
from base import base_twitter_fixture, base_authenticated_fixture


def test_delete_tweet_successful(base_authenticated_fixture, django_app):
    jack = base_authenticated_fixture['jack']

    # Preconditions
    tweet_1 = Tweet.objects.create(user=jack, content='Tweet 1')
    assert Tweet.objects.count() == 1

    resp = django_app.get('/', user=jack)
    form = resp.forms['delete-tweet-form-{}'.format(tweet_1.id)]
    delete_resp = form.submit()

    # Post conditions
    assert delete_resp.status_code == 302
    assert delete_resp.location.endswith('/')
    assert Tweet.objects.count() == 0

def test_user_cant_delete_other_users_tweet(base_authenticated_fixture, django_app):
    jack = base_authenticated_fixture['jack']
    ev = base_authenticated_fixture['ev']

    # Preconditions
    tweet_1 = Tweet.objects.create(user=jack, content='Tweet 1')
    tweet_2 = Tweet.objects.create(user=ev, content="Ev's tweet")
    assert Tweet.objects.count() == 2

    resp = django_app.get('/', user=jack)
    form = resp.forms['delete-tweet-form-{}'.format(tweet_1.id)]
    form.action = '/tweet/{}/delete?next=/'.format(tweet_2.id)
    delete_resp = form.submit(status=403)

    # Post conditions
    assert delete_resp.status_code == 403
    assert Tweet.objects.count() == 2

def test_not_authenticated_user_cant_delete_tweet(base_twitter_fixture, django_app):
    jack = base_twitter_fixture['jack']

    # Preconditions
    tweet_1 = Tweet.objects.create(user=jack, content='Tweet 1')
    assert Tweet.objects.count() == 1
    resp = django_app.get('/jack')
    form = resp.forms.get('delete-tweet-form-{}'.format(tweet_1.id))
    assert form is None
