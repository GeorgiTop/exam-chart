from tests.base.client_set_up import ChartTestCase


class TestProfile(ChartTestCase):
    def test_profile_string_repr(self):
        self.assertEqual(str(self.profile), f'{self.user.username} Profile')

    def test_profile_picture_has_default_picture(self):
        file_name = 'default.png'

        self.assertTrue(str(self.user.profile.image).endswith(file_name))

    def test_profile_posts_per_page_is_default(self):
        default_posts_per_page = 5

        self.assertEqual(self.user.profile.posts_per_page, default_posts_per_page)
