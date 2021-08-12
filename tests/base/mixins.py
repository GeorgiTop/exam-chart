from django.contrib.auth import get_user_model

from chart.news.models import NewsPost
from chart.vlog.models import VlogPost

UserModel = get_user_model()

class UserTestUtils:
    def create_user(self, **kwargs):
        return UserModel.objects.create_user(**kwargs)

class NewsPostTestUtils:
    def create_news_post(self, **kwargs):
        return NewsPost.objects.create(**kwargs)

class VlogPostTestUtils:
    def create_vlog_post(self, **kwargs):
        return VlogPost.objects.create(**kwargs)