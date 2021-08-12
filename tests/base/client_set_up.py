from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class ChartTestCase(TestCase):
    logged_in_user_username = 'TestUser'
    logged_in_user_email = 'test_user@test.us'
    logged_in_user_password = 'Test!ng42'

    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username=self.logged_in_user_username,
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
