# Create your views here.

from django.shortcuts import render_to_response
from models import Media

def index(request):
  if request.POST:
    newrec = request.POST.get("new")

    r = Media(name = newrec)
    r.save()
  
  recs = Media.objects.order_by('name')
  return render_to_response('MyMedia/index.html', recs)


