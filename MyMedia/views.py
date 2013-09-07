# Create your views here.

from django.shortcuts import render
from MyMedia.models import Media

def index(request):
  if request.POST:
    newrec = request.POST.get("new")
    if not Media.objects.filter(name = newrec).count() == 1:
        r = Media(name = newrec)
        r.save()
  recs = Media.objects.order_by('name')
  return render(request, 'MyMedia/index.html', {'recs': recs})
