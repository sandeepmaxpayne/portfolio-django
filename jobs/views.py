from django.shortcuts import render
from .models import Job


def home(request):
    job = Job.objects  # get all the objects
    return render(request, 'jobs/home.html', {'job': job})

