import pytest

from twitter.models import Tweet
from base import base_twitter_fixture, base_authenticated_fixture


def test_user_profile_not_authenticated_shows_tweets(base_twitter_fixture, django_app):
    jack = base_twitter_fixture['jack']
    ev = base_twitter_fixture['ev']

    # Pre conditions - create a few tweets
    Tweet.objects.create(user=jack, content='Tweet 1')
    Tweet.objects.create(user=jack, content='Tweet 2')
    Tweet.objects.create(user=ev, content='My name is Evan')

    resp = django_app.get('/jack')

    # Post conditions
    feed = resp.html.find('div', class_='tweet-feed')

    tweets = feed.find_all('div', class_='tweet-container')
    assert len(tweets) == 2
    first, second = tweets
    assert first.find('div', class_='tweet-content').text == 'Tweet 2'
    assert second.find('div', class_='tweet-content').text == 'Tweet 1'

    # Tweets DON'T have a delete form
    assert first.find('form') is None
    assert second.find('form') is None

    # Ev's tweet is not shown
    assert 'My name is Evan' not in resp.html.text

def test_user_profile_as_authenticated_user_shows_tweets(base_authenticated_fixture, django_app):
    jack = base_authenticated_fixture['jack']
    ev = base_authenticated_fixture['ev']

    # Pre conditions - create a few tweets
    tweet_1 = Tweet.objects.create(user=jack, content='Tweet 1')
    tweet_2 = Tweet.objects.create(user=jack, content='Tweet 2')
    Tweet.objects.create(user=ev, content='My name is Evan')

    resp = django_app.get('/', user=jack)

    # Post conditions
    feed = resp.html.find('div', class_='tweet-feed')

    tweets = feed.find_all('div', class_='tweet-container')
    assert len(tweets) == 2
    first, second = tweets
    assert first.find('div', class_='tweet-content').text == 'Tweet 2'
    assert second.find('div', class_='tweet-content').text == 'Tweet 1'

    # Tweets have a delete form
    assert first.find('form') is not None
    assert second.find('form') is not None

    form = first.find('form')
    assert form.attrs['action'] == "/tweet/{id}/delete?next=/".format(id=tweet_2.id)

    # Ev's tweet is not shown
    assert 'My name is Evan' not in resp.html.text
