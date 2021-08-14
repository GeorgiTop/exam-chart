import os
import random

from django.conf import settings
from django.test.testcases import SerializeMixin
from django.contrib.auth import get_user_model
from chart.users.models import Profile
from tests.base.client_set_up import ChartTestCase


class TestProfileSignals(ChartTestCase):
    def test_profile_is_created_with_user(self):
        self.assertIsInstance(self.profile, Profile)

    def test_user_has_linked_profile(self):
        self.assertIsInstance(self.user.profile, Profile)

class TestFileSignals(SerializeMixin, ChartTestCase):
    lockfile = __file__

    def test_remove_old_profile_picture(self):
        path_to_image_a = 'profile_pics/my_old_file.png'
        path_to_image_b = 'profile_pics/my_new_file.png'
        self.file_one = os.path.join(settings.MEDIA_ROOT, 'profile_pics/my_old_file.png')
        self.file_two = os.path.join(settings.MEDIA_ROOT, 'profile_pics/my_new_file.png')
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.webp')
        file_name = f'{random.randint(1, 10000)}-test_image.webp'
        self.file_a = create_file(self.file_one)
        self.file_b = create_file(self.file_two)
        self.profile.image = path_to_image_a
        self.profile.image = path_to_image_b
        self.profile.save()

        self.assertFalse(os.path.exists(self.file_a))

