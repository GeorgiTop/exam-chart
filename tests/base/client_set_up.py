from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase, Client

from chart.users.models import Profile

UserModel = get_user_model()


class ChartTestCase(TestCase):
    user_username = 'TestUser'
    user_email = 'test_user@test.us'
    user_password = 'Test!ng42'
    # compare_username = 'TestUser_2'
    # compare_email = 'test_user_2@test.us'
    # compare_password = 'Test!ng66'


    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            username=self.user_username,
            email=self.user_email,
            password=self.user_password,
        )
        self.profile = Profile.objects.get(pk=self.user.id)
        self.factory = RequestFactory()
