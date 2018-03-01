from django.contrib import admin
from .models import UserProfile

class UserProfileForm(admin.ModelAdmin):
	list_display = [
		'user',
		'fullName', 
		'address', 
		'gender', 
		'dob', 
		'homePhone', 
		'personalPhone', 
		'emergencyContact', 
		'email', 
		'ppsn', 
		'maritalStatus', 
		'employment', 
		'personalPic'
	]

admin.site.register(UserProfile, UserProfileForm)
