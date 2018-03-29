from base import base_twitter_fixture

def test_user_browsing_profile_is_ok(self):
    index = self.app.get('/', user=self.jack)
    self.assertEqual(index.status_code, 200)

def test_user_browsing_profile_is_sees_tweet_form(self):
    index = self.app.get('/', user=self.jack)
    self.assertEqual(index.status_code, 200)

    form = index.form
    self.assertIsNotNone(form)
    self.assertEqual(form.method, 'POST')
    self.assertEqual(form.action, '')
    content_field = form['content']
    self.assertEqual(content_field.tag, 'textarea')
    self.assertEqual(content_field.name, 'content')
    self.assertEqual(content_field.value, '')

def test_user_browsing_other_user_doesnt_see_form(self):
    index = self.app.get('/evan', user=self.jack)
    self.assertEqual(index.status_code, 200)

    tweet_form = index.html.find('form', class_='tweet-form')
    self.assertIsNone(tweet_form)

def test_user_browsing_own_profile_url_sees_form(self):
    index = self.app.get('/jack', user=self.jack)
    self.assertEqual(index.status_code, 200)

    form = index.form
    self.assertIsNotNone(form)
    self.assertEqual(form.method, 'POST')
    self.assertEqual(form.action, '')
    content_field = form['content']
    self.assertEqual(content_field.tag, 'textarea')
    self.assertEqual(content_field.name, 'content')
    self.assertEqual(content_field.value, '')
