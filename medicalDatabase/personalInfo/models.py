from django.db import models

class GeneralInfo(models.Model):
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

	def __str__(self):
		return self.fullName + ' - ' + self.dob