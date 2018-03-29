import pytest

# class BaseTwitterCloneTestCase(WebTest):
#     def setUp(self):
#         self.jack = User.objects.create_user(
#             username='jack', email='jack@twitter.com', password='coffee')
#         self.ev = User.objects.create_user(
#             username='evan', email='ev@twitter.com', password='coffee')
#
#     def get_session_cookie(self, cookie_name='sessionid'):
#         for cookie in self.app.cookiejar:
#             if cookie.name == cookie_name:
#                 return cookie
#
#     def clear_session_cookie(self):
#         sid_cookie = self.get_session_cookie()
#
#         if not sid_cookie:
#             raise AttributeError("No session cookie found")
#
#         self.app.cookiejar.clear(
#             sid_cookie.domain, sid_cookie.path, sid_cookie.name)


@pytest.fixture
def base_twitter_fixture(client, django_user_model):
    jack = django_user_model.objects.create_user(
        username='jack', email='jack@twitter.com', password='coffee')
    ev = django_user_model.objects.create_user(
        username='evan', email='ev@twitter.com', password='coffee')

    return {
        'jack': jack,
        'ev': ev
    }
