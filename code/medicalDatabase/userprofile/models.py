from djongo import models
from django.db.models.signals import post_save
from djongo.models import forms
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullName = models.CharField(max_length = 250)
	address = models.CharField(max_length = 250)
	gender = models.CharField(max_length = 250)
	dob = models.DateField(blank=True)
	homePhone = models.CharField(max_length = 250)
	personalPhone = models.CharField(max_length = 250)
	emergencyContact = models.CharField(max_length = 250)
	email = models.CharField(max_length = 250)
	ppsn = models.CharField(max_length = 250)
	maritalStatus = models.CharField(max_length = 250)
	employment = models.BooleanField()
	personalPic = models.CharField(max_length = 1000)

	def __str__(self):
		return self.fullName + ' - ' + self.ppsn

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)