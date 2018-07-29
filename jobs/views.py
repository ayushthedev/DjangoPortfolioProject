from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request=request,template_name='jobs/home.html',context={'jobs':jobs})

# Create your views here.
