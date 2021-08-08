from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
from slugify import slugify
from django.contrib.auth.models import User
from chart.users.models import Profile
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class VlogPost(models.Model):
    song_name = models.CharField(max_length=45)
    artist_name = models.CharField(max_length=100)
    lyrics = models.CharField(max_length=110, null=True, blank=True)
    music = models.CharField(max_length=110)
    arranged = models.CharField(max_length=110)
    producer = models.CharField(max_length=110)
    video_url = EmbedVideoField(null=False, blank=False, default='#')
    spotify = models.URLField(null=True, blank=True)
    itunes = models.URLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, editable=True)
    date_posted = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.song_name} - {self.artist_name}'

    def save(self, *args, **kwargs):
        if self.slug is None:
            slug = slugify(self.__str__())
            has_slug = VlogPost.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.__str__()) + '_' + str(count)
                has_slug = VlogPost.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vlog-detail', kwargs={'slug': self.slug})


class Like(models.Model):
    video = models.ForeignKey(VlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
