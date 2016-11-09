from __future__ import unicode_literals

from django.db import models

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    gender = models.CharField(max_length = 10)
    profile_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    @receiver(post_save, sender=User)
    def create_custom_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_custom_user(sender, instance, **kwargs):
    instance.profile.save()
