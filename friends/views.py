# Create your views here.

from django.shortcuts import render
from friends.models import Friendship
from django.contrib.auth.models import User

def index(request):
    userperson = request.user.person
    user = request.user.username

    if request.POST:
        newf = request.POST.get("new")
        lookup = User.objects.filter(username = newf)

        if len(lookup) == 0 or user == newf:
            fr = Friendship.objects.filter(source = userperson)
            friends = map(lambda f: f.target, fr)
            return render(request, 'friends/index.html', {'error': 'that is not a valid user', 'friends': friends, 'username': userperson.firstname, 'points': userperson.currentpoints})

        else:
            u = request.user
            t = lookup[0].person
            friends = Friendship.objects.filter(source = u, target = t)
            if len(friends) > 0:
                fr = Friendship.objects.filter(source = userperson)
                friends = map(lambda f: f.target, fr)
                return render(request, 'friends/index.html', {'error': 'you are already friends', 'friends': friends, 'username': userperson.firstname, 'points': userperson.currentpoints})
            f = Friendship(source = u, target = t)
            f2 = Friendship(source = t, target = u)
            f.save()
            f2.save()
            fr = Friendship.objects.filter(source = userperson)
            friends = map(lambda f: f.target, fr)
            return render(request, 'friends/index.html', {'error': 'successful!', 'friends': friends, 'username': userperson.firstname, 'points': userperson.currentpoints})

    else:
        fr = Friendship.objects.filter(source = userperson)
        friends = map(lambda f: f.target, fr)
        return render(request, 'friends/index.html', {'friends':friends, 'username': userperson.firstname, 'points': userperson.currentpoints})


