# Create your views here.

from django.shortcuts import render_to_response
from models import Media

def index(request):
  recs = Media.objects.order_by('name')
  return render_to_response('MyMedia/index.html', recs)
