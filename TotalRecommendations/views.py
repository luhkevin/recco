# Create your views here.

from django.shortcuts import render
from MyMedia.models import Recommendation, Media

def index(request):
    total_recs = Recommendation.objects.order_by('time')

    #this is filler
    #total_recs = Media.objects.order_by('name')

    return render(request, 'TotalRecommendations/index.html', {'total_recs': total_recs})
