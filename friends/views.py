# Create your views here.

from django.shortcuts import render
from friends.models import Friendship
from django.contrib.auth.models import User

def index(request):
    user = request.user.username
    
    if request.POST:
        newf = request.POST.get("new")
        lookup = User.objects.filter(username = newf)
        
        if len(lookup) == 0:
            fr = Friendship.objects.filter(source__user__username__exact = user)
            friends = map(lambda f: f.target, fr)
            return render(request, 'friends/index.html', {'error': 'that is not a valid user', 'friends': friends}) 
        
        else:
            u = User.objects.get(username = user).person
            t = lookup[0].person
            f = Friendship(source = u, target = t)
            f.save()
            fr = Friendship.objects.filter(source__user__username__exact = user)
            friends = map(lambda f: f.target, fr)
            return render(request, 'friends/index.html', {'error': 'successful!', 'friends': friends})
    
    else:
        fr = Friendship.objects.filter(source__user__username__exact = user)
        friends = map(lambda f: f.target, fr)
        return render(request, 'friends/index.html', {'error':'', 'friends':friends})


