# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from MyMedia.models import *

def index(request):
    userperson = request.user.person
    
    if request.POST:
      newrec = request.POST.get("new")
      medialookup = Media.objects.filter(name = newrec)
      if not medialookup.count() == 1:
          r = Media(name = newrec)
          r.save()
          completedmedia = r
      else: 
          completedmedia = medialookup[0]

      newcompleted = Completed(by = userperson, media = completedmedia, time = timezone.now())
      newcompleted.save()
    recs = userperson.completedmedia.all()
    return render(request, 'MyMedia/index.html', {'recs': recs})
