from base import base_twitter_fixture


def test_user_browsing_profile_is_ok(base_twitter_fixture, client):
    index = client.get('/', user=base_twitter_fixture['jack'])
    assert index.status_code == 200

def test_user_browsing_profile_is_sees_tweet_form(base_twitter_fixture, client):
    index = client.get('/', user=base_twitter_fixture['jack'])
    assert index.status_code == 200

    form = index.form
    assert form is not None
    assert form.method == 'POST'
    assert form.action == ''
    content_field = form['content']
    assert content_field.tag == 'textarea'
    assert content_field.name == 'content'
    assert content_field.value == ''

def test_user_browsing_other_user_doesnt_see_form(base_twitter_fixture, client):
    index = client.get('/evan', user=base_twitter_fixture['jack'])
    assert index.status_code == 200

    tweet_form = index.html.find('form', class_='tweet-form')
    # self.assertIsNone(tweet_form)
    assert tweet_form is not None

def test_user_browsing_own_profile_url_sees_form(base_twitter_fixture, client):
    index = client.get('/jack', user=base_twitter_fixture['jack'])
    assert index.status_code == 200

    form = index.form
    assert form is not None
    assert form.method == 'POST'
    assert form.action == ''
    content_field = form['content']
    assert content_field.tag == 'textarea'
    assert content_field.name == 'content'
    assert content_field.value == ''
