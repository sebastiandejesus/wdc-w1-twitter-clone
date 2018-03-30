import pytest
from django_webtest import WebTest


@pytest.fixture
def base_twitter_fixture(django_app, django_user_model):
    jack = django_user_model.objects.create_user(
        username='jack', email='jack@twitter.com', password='coffee')
    ev = django_user_model.objects.create_user(
        username='evan', email='ev@twitter.com', password='coffee')

    return {
        # 'app': django_app,
        'jack': jack,
        'ev': ev
    }


@pytest.fixture
def base_authenticated_fixture(base_twitter_fixture, django_app):
    jack = base_twitter_fixture['jack']
    form = django_app.get('/login').form
    form['username'] = jack.username
    form['password'] = 'coffee'
    resp = form.submit().follow()

    assert resp.status_code, "Couldn't authenticate user"

    return base_twitter_fixture
