from django.db import models
# from MyMedia.models import *
# from startpage.models import *

# Create your models here.

class Friendship(models.Model):
    source = models.ForeignKey('startpage.Person', related_name = 'source_set')
    target = models.ForeignKey('startpage.Person', related_name = 'target_set')
    recommendations = models.ManyToManyField('MyMedia.Media', through = 'MyMedia.Recommendation')


    def __unicode__(self):
        return self.source + ' to ' + self.target
