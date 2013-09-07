from django.db import models
from MyMedia.models import *
from friends.models import *

# Create your models here.

class Person(models.Model):
    realname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    completed = models.ManyToManyField(Media, through='Completed')
    friends = models.ManyToManyField('self', through='Friendship', symmetrical=False)
    

    def __unicode__(self):
        return self.username
