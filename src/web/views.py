from django.shortcuts import render

# Create your views here.

def home(request):
    template = 'home.html'
    return render(request, template)

def about(request):
    template = 'about.html'
    return render(request, template)
