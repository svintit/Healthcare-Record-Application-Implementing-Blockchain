from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

app_name = 'personalInfo'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^details/$', views.patientDetails, name='patientDetails'),
]