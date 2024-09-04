from django.shortcuts import render

# Create your views here.
def organisationPortal(request):
    return render(request, 'Organisations/organisationPortal.html',context={})