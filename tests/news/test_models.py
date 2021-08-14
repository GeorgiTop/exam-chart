from django.urls import reverse

from chart.news.models import NewsPost
from tests.base.client_set_up import ChartTestCase


class TestNewsPost(ChartTestCase):
    def test_post_string_repr(self):
        post = NewsPost.objects.create(
            title='TestTitle',
            content='Test content.',
            is_public='True',
            author=self.user,
        )
        self.post = post
        self.assertEqual(str(self.post), 'TestTitle', msg='Should be "TestTitle"')

    def test_get_absolute_news_post_url(self):
        post = NewsPost.objects.create(
            title='TestTitle',
            content='Test content.',
            is_public='True',
            author=self.user,
        )
        self.post = post
        self.assertEqual(self.post.get_absolute_url(), reverse('news-detail', args=[str(self.post.id)]))