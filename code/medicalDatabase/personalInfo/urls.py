from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

app_name = 'personalInfo'

urlpatterns = [

	# /personalInfo
	url(r'^$', views.index, name='index'),

	# /personalInfo/ID71
	url(r'^(?P<generalInfo_id>[0-9]+)/$', views.detail, name='detail'),

	url(r'^details/$', views.patientDetails, name='patientDetails'),


]