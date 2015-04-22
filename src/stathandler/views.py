from django.shortcuts import render

# Create your views here.

def statistics(request):
    return render(request, 'statistics.html')


def submit(request):
    return render(request, 'submit.html')
