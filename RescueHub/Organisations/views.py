from django.shortcuts import render, redirect, get_object_or_404
from AidTogether.models import OrganisationProfile
from ReliefCamps.models import  ResourceRequest
from Volunteers.models import VolunteerTasks
from AidTogether.models import ReliefCampProfile



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
    org=ResourceRequest.objects.all()
    camp=ReliefCampProfile.objects.all()
    return render(request, 'Organisations/cardorg.html',{'org':org,'camp':camp})
   
