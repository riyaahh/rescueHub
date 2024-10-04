from django.contrib.auth.models import User
from django.db import models

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)  # Increased length for names
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=20)


    def __str__(self):
        return self.full_name

class OrganisationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name= models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    address = models.TextField()
    phone =  models.CharField(max_length=15)
    org_image=models.ImageField(upload_to='profileimages/')
    
    def __str__(self):
        return self.org_name

class ReliefCampProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    camp_name= models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    address = models.TextField()
    phone =  models.CharField(max_length=15)
    
    def __str__(self):
        return self.org_name

# Create your models here.
