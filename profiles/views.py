# Create your views here.

from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from friends.models import Friendship
from django.contrib.auth.models import User
from MyMedia.models import *

def index(request, target):
    user = request.user.username

    print(target)
    targetlookup = User.objects.filter(username=target)

    if len(targetlookup) == 0:
        return HttpResponseRedirect('/home')


    forwardfriendlookup = Friendship.objects.filter(source__person__user__username__exact = user, target__person__user__username__exact = target)

    if len(forwardfriendlookup) == 0:
        return render(request, 'profiles/index.html', {'error': 'Friendship not found'})

    forwardfriendship = forwardfriendlookup[0]

    backwardfriendlookup = Friendship.objects.filter(source__person__user__username__exact = target, target__person__user__username__exact = user)

    backwardfriendship = backwardfriendlookup[0]

    # find recommendations, to and from
    recto_o = Recommendation.objects.filter(friends = forwardfriendship)
    recfrom_o = Recommendation.objects.filter(friends = backwardfriendship)

# handle form #
    if request.method == "POST":
        fid = request.POST.get("fid")

        ## NEW RECOMMENDATION #
        #######################

        if fid == "1":
            newrecname = request.POST.get("new")

            # lookup media
            medialookup = Media.objects.filter(name = newrecname)

            # create new media if it doesn't exist
            if len(medialookup) == 0 : 
                newmedia = Media(name = newrecname);
                newmedia.save()
                recmedia = newmedia;
            else :
                recmedia = medialookup[0]

            # make new recommendation
            newrec = Recommendation(friends = forwardfriendship, media = recmedia, time = timezone.now())
            newrec.save()
        if fid == '2':
            comps = request.POST.getlist("completed")
            for rec in recto_o:
                for m in comps:
                    if rec.media.name == m:
                        c = Completed(by = targetlookup[0].person, media = rec.media, time = timezone.now())
                        c.save()
                        rec.delete()
    # find recommendations, to and from
    recto_o = Recommendation.objects.filter(friends = forwardfriendship)
    recfrom_o = Recommendation.objects.filter(friends = backwardfriendship)       
    
    # just display stuff

    recto = map(lambda f: f.media, recto_o)
    recfrom = map(lambda f: f.media, recfrom_o)

    return render(request, 'profiles/index.html', {'error':'', 'friend': target, 'recto':recto, 'recfrom':recfrom})



