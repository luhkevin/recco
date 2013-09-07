
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response


def homepage(request):
    return render_to_response('startpage/home.html', {'username':request.user})


