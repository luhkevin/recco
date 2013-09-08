
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response
from MyMedia.models import Recommendation

def homepage(request):
    user = request.user.username
    top_recs_time = Recommendation.objects.filter(friends__target__person__user__username__exact = user).order_by('-time')[:3]
    top_recs_points = Recommendation.objects.filter(friends__target__person__user__username__exact = user).order_by('-points')[:3]
    return render_to_response('startpage/home.html', {'username':user, 'rectime':top_recs_time, 'recpoints':top_recs_points})
