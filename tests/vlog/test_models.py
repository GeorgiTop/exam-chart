from django.urls import reverse
from slugify import slugify

from chart.vlog.models import VlogPost
from tests.base.client_set_up import ChartTestCase


class TestVideoPost(ChartTestCase):
    def test_post_string_repr(self):
        post = VlogPost.objects.create(
            song_name='Testing',
            artist_name='TestUser',
            lyrics='TestUser',
            music='TestUser',
            arranged='TestUser',
            producer='TestUser',
            video_url='https://youtu.be/TestingMeSo',
            spotify='https://spoti.fi/TestingMeSoftly',
            itunes='https://apple.co/TestingMeSoftly',
            author=self.user,
            is_public = True,
        )
        self.post = post
        self.assertEqual(
            str(self.post),
            f'{self.post.song_name} - {self.post.artist_name}',
            msg=f'{self.post.song_name} - {self.post.artist_name}')

    def test_vlog_post_has_slug(self):
        post = VlogPost.objects.create(
            song_name='Testing',
            artist_name='TestUser',
            lyrics='TestUser',
            music='TestUser',
            arranged='TestUser',
            producer='TestUser',
            video_url='https://youtu.be/TestingMeSo',
            spotify='https://spoti.fi/TestingMeSoftly',
            itunes='https://apple.co/TestingMeSoftly',
            author=self.user,
            is_public = True,
        )
        self.post = post
        self.assertEqual(
            str(self.post.slug),
            slugify(f'{self.post.song_name} - {self.post.artist_name}'),
            msg=slugify(f'should be: {self.post.song_name} - {self.post.artist_name}')
        )

    def test_vlog_post_gets_unique_slugs(self):
        valid_post_taking_the_first_slug = VlogPost.objects.create(
            song_name='Testing',
            artist_name='TestUser',
            lyrics='TestUser',
            music='TestUser',
            arranged='TestUser',
            producer='TestUser',
            video_url='https://youtu.be/TestingMeSo',
            spotify='https://spoti.fi/TestingMeSoftly',
            itunes='https://apple.co/TestingMeSoftly',
            author=self.user,
            is_public=True,
        )
        post = VlogPost.objects.create(
            song_name='Testing',
            artist_name='TestUser',
            lyrics='TestUser',
            music='TestUser',
            arranged='TestUser',
            producer='TestUser',
            video_url='https://youtu.be/TestingMeSo',
            spotify='https://spoti.fi/TestingMeSoftly',
            itunes='https://apple.co/TestingMeSoftly',
            author=self.user,
            is_public=True,
        )
        self.post = post
        result = slugify(f'{self.post.song_name} - {self.post.artist_name}')+'_2'
        self.assertEqual(
            str(self.post.slug),
            result,
            msg=f'should be: {result}'
        )

    def test_get_absolute_news_post_url(self):
        post = VlogPost.objects.create(
            song_name='Testing',
            artist_name='TestUser',
            lyrics='TestUser',
            music='TestUser',
            arranged='TestUser',
            producer='TestUser',
            video_url='https://youtu.be/TestingMeSo',
            spotify='https://spoti.fi/TestingMeSoftly',
            itunes='https://apple.co/TestingMeSoftly',
            author=self.user,
            is_public=True,
        )
        self.post = post
        self.assertEqual(self.post.get_absolute_url(), reverse('vlog-detail', args=[str(self.post.slug)]))
