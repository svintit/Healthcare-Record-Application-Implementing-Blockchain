from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request): 
	return render(request, 'personalInfo/index.html', {})

def patientLogin(request):
	return render(request, 'accounts/login.html', {})

def patientLogout(request):
	return render(request, 'accounts/index.html', {})

@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def patientDetails(request):
	return render(request, 'personalInfo/details.html', {})
