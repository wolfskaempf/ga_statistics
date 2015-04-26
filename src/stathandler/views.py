from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import DummyData, Committee, CommitteeStatistic
from .forms import DummyForm

def statistics(request):
    committee = Committee.objects.all()
    committeestatistic = CommitteeStatistic.objects.all()
    return render(request, 'statistics.html', {'committee': committee, 'committeestatistic': committeestatistic})

@login_required(login_url = '/admin/')
def submit(request):
    form = DummyForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'submit.html', context)
