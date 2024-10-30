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

@login_required
def acceptTask(request, id):
    resource_request = get_object_or_404(VolunteerTasks, id=id)
    
    # Check if the user hasn't accepted the task already
    if not resource_request.accepted_by.filter(id=request.user.id).exists():
        resource_request.accepted_by.add(request.user)  # Add current user to accepted_by
        resource_request.status = "Accepted"  # Update the status to "Accepted"
        resource_request.save()  # Save the updated task
    
    return redirect("volunteerTasks")  # Redirect to tasks page
    
def DetailedTask(request):   
    tasks = VolunteerTasks.objects.all()
    return render(request, 'Volunteers/DetailedTask.html',{'tasks':tasks}) 


#