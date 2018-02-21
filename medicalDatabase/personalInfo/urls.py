from django.conf.urls import url
from . import views

app_name = 'personalInfo'

urlpatterns = [
	# /personalInfo
	url(r'^$', views.index, name='index'),

	# /personalInfo/ID71
	url(r'^(?P<generalInfo_id>[0-9]+)/$', views.detail, name='detail'),
] 