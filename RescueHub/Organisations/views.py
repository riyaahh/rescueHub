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

    # Check if the logged-in organization has accepted the task
    org = OrganisationProfile.objects.get(user=request.user)
    
    # Check if the organization has accepted the task
    if not organisation_accepeted_request.objects.filter(org_id=org, resourceRequest_id=task).exists():
        accepted_volunteers = None  # No access to volunteer details if organization hasn't accepted the task
        message = "You are not authorized to view the volunteers for this task."
    else:
        # Fetch the volunteers who accepted this task
        accepted_volunteers = volunteer_accepted_request.objects.filter(resourceRequest_id=task)

        # If there are no accepted volunteers
        if not accepted_volunteers:
            message = "No volunteers have accepted this task yet."
        else:
            message = None

    # Handle POST request to select a volunteer
    if request.method == 'POST':
        volunteer_id = request.POST.get('volunteer_id')  # Get the volunteer ID from the form
        volunteer = VolunteerProfile.objects.get(id=volunteer_id)  # Fetch the volunteer object
        
        # Save the selected volunteer in the FinalVolunteer model
        final_volunteer = FinalVolunteer(volunteer_id=volunteer, resourceRequest=task)
        final_volunteer.save()

        # Redirect to the same page after saving the volunteer selection
        return redirect('task_details', task_id=task_id)

    # Check if a volunteer has already been selected
    final_volunteer = FinalVolunteer.objects.filter(resourceRequest=task).first()
    volunteer_selected = final_volunteer is not None

    return render(request, 'Organisations/ReqTable.html', {
        'task': task, 
        'accepted_volunteers': accepted_volunteers,
        'message': message,
        'volunteer_selected': volunteer_selected
    })
