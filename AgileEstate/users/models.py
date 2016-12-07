from django.contrib.auth.models import Permission, User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=140)
    gender = models.CharField(max_length=140)
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
