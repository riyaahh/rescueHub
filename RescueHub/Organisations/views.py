from django.shortcuts import render
from AidTogether.models import OrganisationProfile

# Create your views here.
def organisationPortal(request):
    organisation=OrganisationProfile.objects.all()
    return render(request, 'Organisations/organisationPortal.html',context={'organisation':organisation})