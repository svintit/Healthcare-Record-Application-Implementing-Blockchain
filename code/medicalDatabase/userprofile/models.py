from djongo import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
	#General Information
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullName = models.CharField(max_length = 250, default='', blank=True)
	address = models.CharField(max_length = 250, default='', blank=True)
	gender = models.CharField(max_length = 250, default='', blank=True)
	dob = models.DateField(blank=True)
	homePhone = models.CharField(max_length = 250, default='', blank=True)
	personalPhone = models.CharField(max_length = 250, default='', blank=True)
	emergencyContact = models.CharField(max_length = 250, default='', blank=True)
	email = models.CharField(max_length = 250, default='', blank=True)
	ppsn = models.CharField(max_length = 250, default='', blank=True)
	maritalStatus = models.CharField(max_length = 250, default='', blank=True)
	employment = models.BooleanField(blank=True)
	personalPic = models.CharField(max_length = 250, default='', blank=True)
	#personalPic = FileField(verbose_name=_("Patient Picture"),
	#	upload_to=upload_to("main.UserProfile.Photo", "profiles"),
	#	format="Image", max_length=255, null=True, blank=True)

	#Current Doctor
	curr_doc_name = models.CharField(max_length = 250, default='', blank=True)
	curr_doc_num = models.CharField(max_length = 250, default='', blank=True)
	curr_doc_email = models.CharField(max_length = 250, default='', blank=True)
	curr_last_visit = models.DateField(blank=True)

	#Previous Doctor
	prev_doc_name = models.CharField(max_length = 250, default='', blank=True)
	prev_doc_num = models.CharField(max_length = 250, default='', blank=True)
	prev_doc_email = models.CharField(max_length = 250, default='', blank=True)
	prev_last_visit = models.DateField(blank=True)

	#Illnesses
	illnesses = models.CharField(max_length = 1000, default='', blank=True)

	#Medication
	medicine = models.CharField(max_length = 1000, default='', blank=True)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
