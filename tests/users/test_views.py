from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from chart.users.views import UserCreateView
from tests.base.client_set_up import ChartTestCase


class UserCreateViewTest(ChartTestCase):
    def test_UserCreateView_get_request(self):
        # Create an instance of a GET request.
        request = self.factory.get('/register')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        # request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        response = UserCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_UserCreateViewTest_post_request(self):
        username = 'TestUser_2'
        email = 'test_user_2@test.us'
        password = 'Test!ng66'
        request = self.factory.post(
            '/register',
            {
                'username': username,
                'email': email,
                'password': password,
            }
        )
        request.user = self.user
        # request.user = AnonymousUser()

        response = UserCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_user_is_loged_in_after_creation(self):
        username = 'TestUser_2'
        email = 'test_user_2@test.us'
        password = 'Test!ng66'
        request = self.factory.post(
            '/register',
            {
                'username': username,
                'email': email,
                'password': password,
            })
        request.user = AnonymousUser()
        response = self.client.get(reverse('register'))
        context = UserCreateView.get_context_data(self)
        self.assertContains(context.context_data, username)

    def test_has_success_message(self):
        username = 'TestUser_2'
        email = 'test_user_2@test.us'
        password = 'Test!ng66'
        request = self.factory.post(
            '/register',
            {
                'username': username,
                'email': email,
                'password': password,
            })

        request.user = AnonymousUser()

        response = UserCreateView.as_view()(request)
        self.assertContains(response['success']['message'], f'Welcome {self.user.username}! Your account has been created!')


class TestProfileView(ChartTestCase):
    def test_profile_returns_200_on_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_uses_profile_html_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile'))

        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_returns_302_without_logged_user_on_GET(self):
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 302)

    def test_profile_redirects_to_user_log_in_if_no_logged_user(self):
        response = self.client.get(reverse('profile'))

        self.assertRedirects(response, '/user/login/?next=/user/profile/')

    # def test_profile_returns_user_info_in_fields(self):
    #     self.client.force_login(self.user)
    #     response = self.client.get(reverse('profile'))
    #
    #     self.assertContains(response, )

