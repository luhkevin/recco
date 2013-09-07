from django.db import models
# from MyMedia.models import *
# from friends.models import *

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    completedmedia = models.ManyToManyField('MyMedia.Media', through='MyMedia.Completed')
    friends = models.ManyToManyField('self', through='friends.Friendship', symmetrical=False)
    

    def __unicode__(self):
        return self.username
