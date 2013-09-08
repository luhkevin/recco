# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from MyMedia.models import *

def index(request):
    userperson = request.user.person
    
    if request.POST:
      newrec = request.POST.get("new")
      medialookup = Completed.objects.filter(media__name__exact = newrec)
      medialookup = map(lambda x: x.media, medialookup)
      if len(medialookup) == 0:
          r = Media(name = newrec)
          r.save()
          newcompleted = Completed(by = userperson, media = r, time = timezone.now())
          newcompleted.save()
    recs = userperson.completedmedia.all()
    return render(request, 'MyMedia/index.html', {'username': userperson.firstname, 'points': userperson.currentpoints, 'recs': recs})
