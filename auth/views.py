# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login

def login_user(request):
    state = "Please log in:"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Successfully logged in."
                return HttpResponseRedirect('/home')
            else: 
                state = "Account inactive."
        else:
            state = "User/pass incorrect."
    c = {'state':state, 'username':username};
    c.update(csrf(request))
    return render_to_response('auth.html',c)
