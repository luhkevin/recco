from django.db import models
from MyMedia.models import Media
from startpage.models import Person

# Create your models here.

class Friendship(models.Model):
    source = models.ForeignKey(Person)
    target = models.ForeignKey(Person)
    recommendations = models.ManyToManyField(Media, though = 'Recommendation')
