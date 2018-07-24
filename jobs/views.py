from django.shortcuts import render

def home(request):
    return render(request=request,template_name='jobs/home.html')

# Create your views here.
