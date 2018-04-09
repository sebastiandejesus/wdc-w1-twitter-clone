import pytest
from base import base_twitter_fixture, base_authenticated_fixture


def test_user_browsing_profile_sees_tweet_form(base_authenticated_fixture, django_app):
    index = django_app.get('/', user=base_authenticated_fixture['jack'])
    assert index.status_code == 200

    form = index.form
    assert form is not None
    assert form.method == 'POST'
    assert form.action == ''
    content_field = form['content']
    assert content_field.tag == 'textarea'
    assert content_field.name == 'content'
    assert content_field.value == ''


def test_user_browsing_other_user_doesnt_see_form(base_authenticated_fixture, django_app):
    index = django_app.get('/evan', user=base_authenticated_fixture['jack'])
    assert index.status_code == 200

    tweet_form = index.html.find('form', class_='tweet-form')
    assert tweet_form is None


def test_user_browsing_own_profile_url_sees_form(base_authenticated_fixture, django_app):
    index = django_app.get('/jack', user=base_authenticated_fixture['jack'])
    assert index.status_code == 200

    form = index.form
    assert form is not None
    assert form.method == 'POST'
    assert form.action == ''
    content_field = form['content']
    assert content_field.tag == 'textarea'
    assert content_field.name == 'content'
    assert content_field.value == ''
