from django.shortcuts import render, redirect, get_object_or_404
from AidTogether.models import VolunteerProfile,OrganisationProfile
from django.contrib.auth.decorators import login_required 
from ReliefCamps.models import ResourceRequest
from Volunteers.models import VolunteerTasks
from AidTogether.models import OrganisationProfile
from Volunteers.models import volunteer_accepted_request
from Organisations.models import organisation_accepeted_request


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
    return redirect("cardView")

@login_required
def acceptTask(request, id):
    resource_request = get_object_or_404(VolunteerTasks, id=id)
      # Check if the user hasn't accepted the task already
    if not resource_request.accepted_by.filter(id=request.user.id).exists():
        resource_request.accepted_by.add(request.user)  # Add current user to accepted_by
        resource_request.status = "Accepted"  # Update the status to "Accepted"
        resource_request.save()  # Save the updated task
    return redirect("cardView")

    
def card(request):
    tasks = VolunteerTasks.objects.all()
    
    return render(request, "Volunteers/card.html",{'tasks':tasks})

def Taskrequests(request):
    return render(request, "Volunteers/Taskrequests.html",context={})

def card(request):
    # Fetch requests with 'Accepted' status
    accepted_req = organisation_accepeted_request.objects.filter(resourceRequest_id__status='Accepted')
    
    # Get IDs of requests already accepted by the current volunteer
    accepted_resource_ids = volunteer_accepted_request.objects.filter(volunteer_id=request.user.id).values_list('resourceRequest_id', flat=True)
    
    # Exclude requests already accepted by the current volunteer
    volunteer_task = accepted_req.exclude(resourceRequest_id__in=accepted_resource_ids) 
    return render(request, "Volunteers/card.html", {'accepted_requests': volunteer_task})


def volunteer_accept_request(request, request_id):
    volunteer = VolunteerProfile.objects.get(user=request.user)
    # Retrieve the resource request based on the given request_id
    resource = ResourceRequest.objects.get(id=request_id)
    
    # Create a new acceptance entry, allowing multiple volunteers to accept the same request
    volunteer_accept = volunteer_accepted_request(
        resourceRequest_id=resource,
        volunteer_id=volunteer
    )
    volunteer_accept.save()

    return redirect('card')


