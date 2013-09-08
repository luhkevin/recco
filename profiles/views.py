# Create your views here.

from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from friends.models import Friendship
from django.contrib.auth.models import User
from MyMedia.models import *

def index(request, target):
    user = request.user.username

    targetlookup = User.objects.filter(username=target)

    if len(targetlookup) == 0:
        return HttpResponseRedirect('/home')

    userperson = request.user.person
    targetperson = targetlookup[0].person


    forwardfriendlookup = Friendship.objects.filter(source = userperson, target = targetperson)

    if len(forwardfriendlookup) == 0:
        return render(request, 'profiles/index.html', {'error': 'Friendship not found', 'username': userperson.firstname, 'points': userperson.currentpoints})

    forwardfriendship = forwardfriendlookup[0]

    backwardfriendlookup = Friendship.objects.filter(source = targetperson, target = userperson)

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
            newrecptstr = request.POST.get("newpoints")
            newcomment = request.POST.get("comment")

            newrecpoints = int(newrecptstr)

            if userperson.currentpoints < newrecpoints:
                return render(request, 'profiles/index.html', {'error':'not enough points', 'friend': target, 'recto':recto_o, 'recfrom':recfrom_o, 'username': userperson.firstname, 'points': userperson.currentpoints})
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
            newrec = Recommendation(friends = forwardfriendship, points = newrecpoints, media = recmedia, time = timezone.now(), comment = newcomment)
            newrec.save()

            userperson.currentpoints -= newrecpoints
            userperson.save()
        if fid == '2':
            comps = request.POST.getlist("completed")
            for rec in recto_o:
                for m in comps:
                    if rec.media.name == m:
                        targetperson.currentpoints += rec.points
                        targetperson.lifetimepoints += rec.points
                        targetperson.save()
                        c = Completed(by = targetperson, media = rec.media, time = timezone.now())
                        c.save()
                        rec.delete()
                        break
    # find recommendations, to and from
    recto_o = Recommendation.objects.filter(friends = forwardfriendship)
    recfrom_o = Recommendation.objects.filter(friends = backwardfriendship)       
    # just display stuff

    recto = map(lambda f: f.media, recto_o)
    recfrom = map(lambda f: f.media, recfrom_o)

    return render(request, 'profiles/index.html', {'friend': targetperson, 'recto':recto_o, 'recfrom':recfrom_o, 'username': userperson.firstname, 'points': userperson.currentpoints})

