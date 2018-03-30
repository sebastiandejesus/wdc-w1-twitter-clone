import pytest
from base import base_twitter_fixture


@pytest.mark.django_db
def test_home_view_redirects_if_not_authenticated(base_twitter_fixture, django_app):
    "Should be redirected if trying to browse the home page"
    index = django_app.get('/')
    assert index.status_code == 302
    assert index.url.endswith('/login?next=/')


@pytest.mark.django_db
def test_profile_view_redirects_if_not_authenticated(base_twitter_fixture, django_app):
    "Should see the profile even if not authenticated"
    index = django_app.get('/jack')
    assert index.status_code == 200


@pytest.mark.django_db
def test_login_ok_if_not_authenticated(base_twitter_fixture, django_app):
    "Should see the login page if not authenticated"
    index = django_app.get('/login')
    assert index.status_code == 200
