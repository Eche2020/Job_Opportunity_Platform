# jobs/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'jobs/index.html')

def job_list(request):
    return render(request, 'jobs/job_list.html')

def job_detail(request):

    return render(request, 'jobs/job_detail.html')

def profile(request):
    return render(request, 'jobs/profile.html')

def login(request):
  return render(request, 'jobs/login.html')
  

def signIn(request):
  return render(request, 'jobs/login.html')