import operator
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required


# Create your views here.

from .models import Committee, CommitteeStatistic
from .forms import CommitteeStatisticForm




def committee_list(request):
    """ This view serves the list of all the committees displayed after clicking Statistics """

    committee = Committee.objects.order_by('gaPosition')
    return render(request, 'committee_list.html', {'committee': committee})




def committee_single(request, pk):
    """ This view serves the actual statistics for each proposing committee """
    committees = Committee.objects.all()

    committee = Committee.objects.get(pk=pk)

    all_points = CommitteeStatistic.objects.filter(committee=pk)

    recent_points = all_points[:5]

    return render(request, 'committee_single.html', {'committee': committee, 'pk': pk, 'recent_points': recent_points})






@login_required(login_url = '/login/')
def submit(request):
    """ This view requires the user to be logged in. When it's finished, it'll show a form which can be used to submit the data which is displayed in the committee_single view """
    form = CommitteeStatisticForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'submit.html', context)
