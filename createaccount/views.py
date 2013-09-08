# Create your views here.


from django.http import HttpResponseRedirect
from django.shortcuts import render
from createaccountform import CreateAccountForm

def createaccount(request):
    form = CreateAccountForm();
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            # Process stuff
            form.save();

            # successful user account creation
            return HttpResponseRedirect('../')
        else:
            print('qq form isn\'t valid')
            form = CreateAccountForm()

    return render(request, 'createaccount/createaccount.html', {'form':form})

