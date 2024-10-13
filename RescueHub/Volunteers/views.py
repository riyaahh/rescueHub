from django.shortcuts import render,redirect
from AidTogether.models import VolunteerProfile,OrganisationProfile
from django.contrib.auth.decorators import login_required 
from Volunteers.models import VolunteerTasks



# Create your views here.
def VolunteerPortal(request):
    volunteer=VolunteerProfile.objects.all()
    return render(request, "Volunteers/VolunteerPortal.html",{'volunteer':volunteer})

def volunteerTask(request):   
    tasks = VolunteerTasks.objects.all()
    return render(request, 'Volunteers/volunteertasks.html',{'tasks':tasks}) 


#