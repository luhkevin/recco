# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render

def create_user(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process stuff

            # successful user account creation
            return HttpResponseRedirect('/accountcreated/')
        else: 
            form = ContactForm()
        return render(request, 'create_user.html', {'form':form})
        
