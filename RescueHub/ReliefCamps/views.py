from django.shortcuts import render
from AidTogether.models import ReliefCampProfile

def CampPortal(request):
    camp=ReliefCampProfile.objects.all()
    return render(request,"ReliefCamps/CampPortal.html",context={'camp':camp})
def RequestForm(request):
    return render(request, 'ReliefCamps/RequestForm.html',context={})