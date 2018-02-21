from django.http import HttpResponse
from django.template import loader
from .models import GeneralInfo

def index(request): 
	all_generalInfo = GeneralInfo.objects.all()
	template = loader.get_template('')
	return HttpResponse(html)

def detail(request, generalInfo_id):
	return HttpResponse("<h2>Details for user id: " + str(generalInfo_id) + "</h2>")

