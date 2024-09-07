from django.contrib.auth.models import User
from django.db import models

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)  # Increased length for names
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=(
        ('volunteer', 'Volunteer'),
        ('organisation', 'Organisation'),
        ('relief_camp', 'Relief Camp'),
    ),default='volunteer')

    def __str__(self):
        return self.full_name

# class OrganisationProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     contact_person = models.CharField(max_length=100)
#     address = models.TextField()

# class ReliefCampProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     contact_person = models.CharField(max_length=100)
#     address = models.TextField()

# Create your models here.
