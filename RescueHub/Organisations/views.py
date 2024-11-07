from django.shortcuts import render, redirect, get_object_or_404
from AidTogether.models import OrganisationProfile, VolunteerProfile
from ReliefCamps.models import  ResourceRequest
from Volunteers.models import VolunteerTasks, volunteer_accepted_request, FinalVolunteer
from AidTogether.models import ReliefCampProfile
from Organisations.models import organisation_accepeted_request


# Create your views here.
def organisationPortal(request):
    organisation=OrganisationProfile.objects.all()
    return render(request, 'Organisations/organisationPortal.html',context={'organisation':organisation})

def ReqTable(request):   
    data = ResourceRequest.objects.all()
    return render(request, 'Organisations/ReqTable.html',context={'data':data}) 

def denyRequest(request, id):
    resource_request = get_object_or_404(ResourceRequest, id=id)
    resource_request.status = "Denied"  # Assuming you have a 'status' field in your model
    resource_request.save()  # Save the updated status
    return redirect("cardorg")

def acceptRequest(request, id):
    resource_request = get_object_or_404(ResourceRequest, id=id)
    resource_request.status = "Accepted"  # Update the status to "Accepted"
    resource_request.save()  # Save the updated status

    # Now create an entry in the VolunteerTasks table
    VolunteerTasks.objects.create(
        receivers_id=resource_request,  # Link to the ResourceRequest
        org_id=request.user.organisationprofile,  # Assuming the user is linked to an organisation profile
        status="Accepted"  # Set the status to "Accepted"
    )

    return redirect("cardorg")  # Redirect as needed

def Reqportal(request):
    data = ResourceRequest.objects.all()
    return render(request, 'Organisations/Reqportal.html',context={'data':data}) 


def cardorg(request):
    org = OrganisationProfile.objects.get(user=request.user)
    # Fetch all resource requests
    resource_request = ResourceRequest.objects.all()
    # Get IDs of requests accepted by any organization
    accepted_requests = organisation_accepeted_request.objects.values_list('resourceRequest_id', flat=True)
    
    return render(request, 'Organisations/cardorg.html', {
        'resource_request': resource_request,
        'accepted_requests': accepted_requests,
    })

def org_accept_request(request, request_id):
    org = OrganisationProfile.objects.get(user=request.user)
    resource_request = ResourceRequest.objects.get(id=request_id)
    resource_request.status = "Accepted"
    resource_request.save()

    # Only create an acceptance record if one doesn't already exist
    if not organisation_accepeted_request.objects.filter(resourceRequest_id=resource_request).exists():
        accept = organisation_accepeted_request(org_id=org, resourceRequest_id=resource_request)
        accept.save()
    
    return redirect('cardorg')

def task_details(request, task_id):
    # Fetch the task by its ID
    task = ResourceRequest.objects.get(id=task_id)

    # Fetch the logged-in volunteer
    volunteer = VolunteerProfile.objects.get(user=request.user)

    # Check if this volunteer is assigned to the task
    try:
        final_volunteer = FinalVolunteer.objects.get(volunteer_id=volunteer, resourceRequest_id=task)
        message = "You have been assigned to this task."
    except FinalVolunteer.DoesNotExist:
        final_volunteer = None
        message = "You are not assigned to this task."

    return render(request, 'Volunteers/volunteertasks.html', {
        'task': task,
        'message': message,
        'final_volunteer': final_volunteer,
    })

