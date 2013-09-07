from django.db import models
# from startpage.models import *
# from friends.models import *
# Create your models here.

class Media(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Recommendation(models.Model):
    friends = models.ForeignKey('friends.Friendship')
    media = models.ForeignKey('MyMedia.Media')
    time = models.DateTimeField('date recommended')

class Completed(models.Model):
    by = models.ForeignKey('startpage.Person')
    media = models.ForeignKey('MyMedia.Media')
    time = models.DateTimeField('date completed')

    def __unicode__(self):
        return self.name
