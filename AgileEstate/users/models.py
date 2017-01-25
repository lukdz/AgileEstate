from django.contrib.auth.models import Permission, User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=140)
    gender = models.CharField(max_length=140)
    firstname = models.CharField(max_length=140)
    lastname = models.CharField(max_length=140)
    profile_picture = models.CharField(max_length=140)

    def __unicode__( self ):
        return self.firstname + " " + self.lastname

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
