from django.contrib import admin
from .models import GeneralInfo

admin.site.register(GeneralInfo)
admin.site.site_header = 'Doctor Login - Medical Database'
admin.site.site_title = 'Doctor Login - Medical Database'
admin.site.site_url = 'http://127.0.0.1:8000/personalInfo'
admin.site.index_title = 'User Information'
