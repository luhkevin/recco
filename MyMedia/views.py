# Create your views here.

from django.shortcuts import render
from MyMedia.models import Media

def index(request)
    userperson = request.user.person
    
    if request.POST:
      newrec = request.POST.get("new")
      if not Media.objects.filter(name = newrec).count() == 1:
          r = Media(name = newrec)
          r.save()
    recs = userperson.completedmedia.objects.order_by('name')
    return render(request, 'MyMedia/index.html', {'recs': recs})
