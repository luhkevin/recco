# Create your views here.
from django.utils import timezone
from django.shortcuts import render
from MyMedia.models import Recommendation, Media

def index(request):
    user = request.user.username
    total_recs = Recommendation.objects.filter(friends__target__person__user__username__exact = user).order_by('-time')
    #this is filler
    #total_recs = Media.objects.order_by('name')

    return render(request, 'TotalRecommendations/index.html', {'total_recs': total_recs})
