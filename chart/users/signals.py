import os
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=Profile)
def remove_old_profile_picture(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    # comparing the new file with the old one and default profile picture name
    default_profile_image = 'default.png'
    file = instance.image
    if not old_file == file:
        if os.path.isfile(old_file.path) and old_file != default_profile_image:
            os.remove(old_file.path)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
