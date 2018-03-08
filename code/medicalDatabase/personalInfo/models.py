from djongo import models
from djongo.models import forms

class UserProfile(models.Model):
	#General Information
	fullName = models.CharField(max_length = 250)
	address = models.CharField(max_length = 250)
	gender = models.CharField(max_length = 250)
	dob = models.CharField(max_length = 250)
	homePhone = models.CharField(max_length = 250)
	personalPhone = models.CharField(max_length = 250)
	emergencyContact = models.CharField(max_length = 250)
	email = models.CharField(max_length = 250)
	ppsn = models.CharField(max_length = 250)
	maritalStatus = models.CharField(max_length = 250)
	employment = models.CharField(max_length = 250)
	personalPic = models.CharField(max_length = 1000)

