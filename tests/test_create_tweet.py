import pytest

from twitter.models import Tweet
from base import base_twitter_fixture, base_authenticated_fixture


def test_user_cant_post_tweet_to_wrong_URL(base_authenticated_fixture, django_app):
    index = django_app.get('/', user=base_authenticated_fixture['jack'])
    form = index.form
    form['content'] = 'rmotr.com - Web Dev Django'
    form.action = '/evan'
    response = form.submit(status=403)
    assert response.status_code == 403

def test_user_cant_post_tweet_with_more_than_140_chars(base_authenticated_fixture, django_app):
    # Pre conditions
    assert Tweet.objects.count() == 0

    index = django_app.get('/', user=base_authenticated_fixture['jack'])
    form = index.form
    form['content'] = 'a' * 141
    response = form.submit()
    div = response.form.html.find('div', class_='has-error')
    assert div is not None
    span = div.find('span')
    assert span is not None
    assert span.text == 'Ensure this value has at most 140 characters (it has 141).'

    # Post conditions
    assert Tweet.objects.count() == 0

def test_user_can_post_tweet_successfully(base_authenticated_fixture, django_app):
    # Pre conditions
    assert Tweet.objects.count() == 0

    index = django_app.get('/', user=base_authenticated_fixture['jack'])
    form = index.form
    form['content'] = 'rmotr.com - Web Dev Django'
    response = form.submit()

    # Post conditions
    assert Tweet.objects.count() == 1

    messages_div = response.html.find('div', class_='messages')
    assert messages_div is not None
    success_div = messages_div.find('div', class_='alert-success')
    assert success_div is not None
