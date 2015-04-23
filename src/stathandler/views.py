from django.shortcuts import render, render_to_response

# Create your views here.

from .models import DummyData

def statistics(request):
    dummynumbers = DummyData.objects.all()
    return render_to_response('statistics.html', {'numbers': dummynumbers})


def submit(request):
    return render(request, 'submit.html')
