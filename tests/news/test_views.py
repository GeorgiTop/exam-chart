from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from chart.news.models import NewsPost
from chart.news.views import get_user_settings_posts_per_page
from tests.base.client_set_up import ChartTestCase


class NewsPostViewsTest(ChartTestCase):
    def test_logged_user_settings_posts_per_page(self):
        self.client.force_login(self.user)
        post_per_page = User.objects.get(pk=1).profile.posts_per_page = 8
        user = User.objects.get(pk=1)
        result = get_user_settings_posts_per_page(self.user)
        self.assertEqual(self.profile.posts_per_page, result)

    def test_user_settings_posts_per_page(self):
        result = get_user_settings_posts_per_page(self.user)
        self.assertEqual(self.profile.posts_per_page, result)


    def test_news_post_list_without_logged_user_get(self):
        response = self.client.get(reverse('news-home'))

        self.assertEqual(response.status_code, 302)

    def test_news_post_list_user_logged_in_get(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('news-home'))

        self.assertEqual(response.status_code, 200)


