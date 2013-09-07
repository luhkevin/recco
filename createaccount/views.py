# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render
from createuser import CreateUserForm

def createaccount(request):
    form = CreateUserForm();
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Process stuff
            form.save();

            # successful user account creation
            return HttpResponseRedirect('../login')
        else: 
            print('qq form isn\'t valid')
            form = CreateUserForm()

    return render(request, 'createaccount/create_account.html', {'form':form})
        
