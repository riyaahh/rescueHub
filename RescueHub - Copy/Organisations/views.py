from django.shortcuts import render, redirect, get_object_or_404
from AidTogether.models import OrganisationProfile
from ReliefCamps.models import  ResourceRequest



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
    return redirect("ReqTable")

def acceptRequest(request, id):
    resource_request = get_object_or_404(ResourceRequest, id=id)
    resource_request.status = "Accepted"  # Assuming you have a 'status' field
    resource_request.save()  # Save the updated status
    return redirect("ReqTable")
