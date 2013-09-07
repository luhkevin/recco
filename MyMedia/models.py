from django.db import models
from startpage.models import Person
from friends.models import Friendship
# Create your models here.

class Media(models.Model):
    name = models.CharField(max_length=50)

class Recommendation(models.Model):
    friends = models.ForeignKey(Friendship)
    media = models.ForeignKey(Media)
    time = models.DateTimeField('date recommended')

class Completed(models.Model)
    by = models.ForeignKey(Person)
    media = models.ForeignKey(Media)
    time = models.DateTimeField('date completed')

