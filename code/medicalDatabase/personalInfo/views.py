from django.shortcuts import render, get_object_or_404
from .models import GeneralInfo

def choose(request): 
	all_generalInfo = GeneralInfo.objects.all()
	return render(request, 'personalInfo/personalInfo.html', { 'all_generalInfo': all_generalInfo })

def detail(request, generalInfo_id):
	generalInfo = get_object_or_404(GeneralInfo, pk=generalInfo_id)
	return render(request, 'personalInfo/details.html', { 'generalInfo': generalInfo, })

def index(request): 
	return render(request, 'personalInfo/index.html', {})

def patientLogin(request):
	return render(request, 'accounts/login.html', {})
