from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ReliefCamps.models import ResourceRequest
from AidTogether.models import OrganisationProfile, VolunteerProfile

# Create your models here.
class VolunteerTasks(models.Model):
    receivers_id=models.ForeignKey(ResourceRequest,on_delete=models.CASCADE)
    org_id=models.ForeignKey(OrganisationProfile,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Accepted", "Accepted"), ("Denied", "Denied")], default="Pending")
    accepted_by = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)  # Allows multiple users

    
class volunteer_accepted_request(models.Model):
    volunteer_id = models.ForeignKey(VolunteerProfile, on_delete=models.CASCADE)
    resourceRequest_id=models.ForeignKey(ResourceRequest,on_delete=models.CASCADE)
    
class FinalVolunteer(models.Model):
    volunteer_id = models.ForeignKey(VolunteerProfile, on_delete=models.CASCADE)
    resourceRequest = models.ForeignKey(ResourceRequest, on_delete=models.CASCADE)
    
