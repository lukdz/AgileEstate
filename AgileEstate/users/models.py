from django.contrib.auth.models import Permission, User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    location = models.CharField(max_length=140)
    gender = models.CharField(max_length=140)
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username
