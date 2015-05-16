from django.shortcuts import render

# Create your views here.

# We might add a Class based view here later so only one view is needed for all completely static pages.

def home(request):
    template = 'home.html'
    return render(request, template)

def about(request):
    template = 'about.html'
    return render(request, template)
