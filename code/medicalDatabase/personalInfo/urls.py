from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import include, path
from django.contrib.auth import views as auth_views

app_name = 'personalInfo'

urlpatterns = [

	url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
	# /personalInfo
	url(r'^$', views.index, name='index'),

	# /personalInfo/ID71
	url(r'^(?P<generalInfo_id>[0-9]+)/$', views.detail, name='detail'),
]