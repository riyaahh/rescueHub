from django.db import models
from django.contrib.auth.models import User
from AidTogether.models import ReliefCampProfile

# Model to capture resource requests
class ResourceRequest(models.Model):
    URGENCY_CHOICES = [
        ('IMMEDIATE', 'Immediate'),
        ('24_HOURS', 'Next 24 Hours'),
        ('WEEK', 'Within a Week'),
    ]

    RESOURCE_TYPES = [
        ('FOOD', 'Food'),
        ('MEDICAL_SUPPLIES', 'Medical Supplies'),
        ('VOLUNTEERS', 'Volunteers'),
        ('EQUIPMENT', 'Equipment'),
        ('SHELTER', 'Shelter'),
    ]

    camp = models.ForeignKey(ReliefCampProfile, on_delete=models.CASCADE, related_name="resource_requests")
    requester_name = models.CharField(max_length=255)
    requester_phone = models.CharField(max_length=15)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    quantity = models.PositiveIntegerField()
    request_details = models.TextField()
    delivery_address = models.TextField()
    requested_by_date = models.DateField()
    urgency_level = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Accepted", "Accepted"), ("Denied", "Denied")], default="Pending")

    def __str__(self):
        return f"Request by {self.requester_name} for {self.camp_name}"

