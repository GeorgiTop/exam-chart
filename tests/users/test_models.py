from os.path import join

from django.conf import settings

from chart.users.models import Profile
from tests.base.client_set_up import ChartTestCase


class TestProfile(ChartTestCase):
    def test_profile_string_repr(self):
        profile = Profile.objects.create(
            user=self.user
        )

        self.assertEqual(str(profile), f'{self.user.username} Profile')

    def test_profile_picture_has_default_picture(self):
        profile = Profile.objects.create(
            user=self.user
        )
        file_name = 'default.png'

        self.assertTrue(str(profile.image).endswith(file_name))

    def test_profile_posts_per_page_is_default(self):
        profile = Profile.objects.create(
            user=self.user
        )
        default_posts_per_page = 5

        self.assertEqual(profile.posts_per_page, default_posts_per_page)

