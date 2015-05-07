from django.shortcuts import render, HttpResponseRedirect

from .forms import LoginForm
from django.contrib.auth import get_user_model, authenticate, login, logout


# Create your views here.

def ga_login(request):
# This view is shown, when a user tries to view the submit form, but isn't logged in. After they log in, they'll be taken to /submit/.
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print username, password

        user = authenticate(username=username,
                            password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/submit/')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

    template = 'login.html'
    context = {'form': form}
    return render(request, template, context)


def ga_logout(request):
    # If the user visits /logout/ he will be logged out.
    
    logout(request)
    return HttpResponseRedirect('/')
