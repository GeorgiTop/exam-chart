# from django.db import models
#
# # Create your models here.
#
#
# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     songs = models.ManyToManyField(Song)
#
#
# class Song(models.Model):
#     name = models.CharField(max_length=45)
#     artist_name = models.CharField(max_length=100)
#     artists = models.ManyToManyField(Artist)
#     lyrics = models.CharField(max_length=110)
#     composer = models.CharField(max_length=110)
#     arranged = models.CharField(max_length=110)
#     producer = models.CharField(max_length=110)
#     youtube = models.URLField(null=False)
#     spotify = models.URLField()
#     itunes = models.URLField()
#     picture = models.ImageField(upload_to='staticfiles')
#
#
