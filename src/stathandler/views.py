from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

from .models import DummyData
from .forms import DummyForm

def statistics(request):
    dummynumbers = DummyData.objects.all()
    return render(request, 'statistics.html', {'numbers': dummynumbers})


def submit(request):
    form = DummyForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'submit.html', context)
