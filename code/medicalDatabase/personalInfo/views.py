from django.shortcuts import render, get_object_or_404
from .models import GeneralInfo
from django.contrib.auth.decorators import login_required


def detail(request, generalInfo_id):
	generalInfo = get_object_or_404(GeneralInfo, pk=generalInfo_id)
	return render(request, 'personalInfo/details.html', { 'generalInfo': generalInfo, })

def index(request): 
	return render(request, 'personalInfo/index.html', {})

def patientLogin(request):
	return render(request, 'accounts/login.html', {})

@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def patientDetails(request):
	return render(request, 'personalInfo/details.html', {})

