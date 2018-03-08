from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template.response import TemplateResponse
from .models import UserProfile
from django.core import serializers
from django.http import JsonResponse

def index(request): 
	return render(request, 'personalInfo/index.html', {})

def patientLogin(request):
	return render(request, 'accounts/login.html', {})

def patientLogout(request):
	return render(request, 'accounts/index.html', {})

@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def userprofile(request):
	profile = request.user.userprofile
	return TemplateResponse(request, 'personalInfo/details.html', {"profile": profile}) 

def get_modelAPI(request):
    UserProfile_json = serializers.serialize("json", UserProfile.objects.all())
    data = {"UserProfile_json": UserProfile_json}
    return JsonResponse(data)