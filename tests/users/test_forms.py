from chart.users.models import Profile
from django.urls import reverse


def test_profile_saves_uploaded_picture(self):
    path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.webp')
    file_name = f'{random.randint(1, 10000)}-test_image.webp'
    file = SimpleUploadedFile(
        name=file_name,
        content=open(path_to_image, 'rb').read(),
        content_type='image/jpeg')

    self.client.force_login(self.user)
    profile = Profile.objects.get(pk=self.user.id)
    self.assertTrue(str(profile.profile_image).endswith(file_name))