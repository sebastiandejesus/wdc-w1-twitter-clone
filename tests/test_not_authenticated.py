from base import base_twitter_fixture


def test_home_view_redirects_if_not_authenticated(base_twitter_fixture, client):
    "Should be redirected if trying to browse the home page"
    index = client.get('/')
    assert index.status_code == 302
    assert index.url.endswith('/login?next=/')


def test_profile_view_redirects_if_not_authenticated(base_twitter_fixture, client):
    "Should see the profile even if not authenticated"
    index = client.get('/jack')
    assert index.status_code == 200


def test_login_ok_if_not_authenticated(base_twitter_fixture, client):
    "Should see the login page if not authenticated"
    index = client.get('/login')
    assert index.status_code == 200
