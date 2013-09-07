from django.db import models
from django.contrib.auth.models import User
# from MyMedia.models import *
# from friends.models import *

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    user = models.OneToOneField(User, primary_key=True)

    # Reverse lookup done by: User.objects.get(pk=1)

    completedmedia = models.ManyToManyField('MyMedia.Media', through='MyMedia.Completed')
    friends = models.ManyToManyField('self', through='friends.Friendship', symmetrical=False)
    

    def __unicode__(self):
        return self.username
