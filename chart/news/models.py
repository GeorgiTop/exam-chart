from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class NewsPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_per_page = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
