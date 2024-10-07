from django.shortcuts import render, redirect
from AidTogether.models import OrganisationProfile
from ReliefCamps.models import  ResourceRequest



# Create your views here.
def organisationPortal(request):
    organisation=OrganisationProfile.objects.all()
    return render(request, 'Organisations/organisationPortal.html',context={'organisation':organisation})
def ReqTable(request):   
    data = ResourceRequest.objects.all()
    return render(request, 'Organisations/ReqTable.html',context={'data':data})  
