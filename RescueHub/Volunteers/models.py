from django.db import models
from ReliefCamps.models import ResourceRequest
from AidTogether.models import OrganisationProfile

# Create your models here.
class VolunteerTasks(models.Model):
    receivers_id=models.ForeignKey(ResourceRequest,on_delete=models.CASCADE)
    org_id=models.ForeignKey(OrganisationProfile,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[ ("Accepted", "Accepted"),("Denied", "Denied")], default="Denied")

    def __str__(self):
        return f"Request by {self.receivers_id} by {self.org_id}"
