from django.shortcuts import render, redirect, get_object_or_404
from AidTogether.models import VolunteerProfile,OrganisationProfile
from django.contrib.auth.decorators import login_required 
from Volunteers.models import VolunteerTasks



# Create your views here.
def VolunteerPortal(request):
    volunteer=VolunteerProfile.objects.all()
    return render(request, "Volunteers/VolunteerPortal.html",{'volunteer':volunteer})

def volunteerTasks(request):   
    tasks = VolunteerTasks.objects.all()
    return render(request, 'Volunteers/volunteertasks.html',{'tasks':tasks}) 

def denyTask(request, id):
    resource_request = get_object_or_404(VolunteerTasks, id=id)
    resource_request.status = "Denied"  # Assuming you have a 'status' field in your model
    resource_request.save()  # Save the updated status
    return redirect("volunteerTasks")

def acceptTask(request, id):
    resource_request = get_object_or_404(VolunteerTasks, id=id)
    resource_request.status = "Accepted"  # Update the status to "Accepted"
    resource_request.save() 
    return redirect("volunteerTasks")

def Taskrequests(request):
    return render(request, "Volunteers/Taskrequests.html",context={})

def card(request):
    return render(request, "Volunteers/card.html",context={})
    


#