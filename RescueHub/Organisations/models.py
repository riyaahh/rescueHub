from django.db import models
from ReliefCamps.models import ResourceRequest
from AidTogether.models import OrganisationProfile
from datetime import datetime
# Create your models here.

class organisation_accepeted_request(models.Model):
    resourceRequest_id=models.ForeignKey(ResourceRequest,on_delete=models.CASCADE)
    org_id=models.ForeignKey(OrganisationProfile,on_delete=models.CASCADE)
    org_accepted_date = models.DateTimeField(default=datetime.now())
    


