from django.shortcuts import render
from AidTogether.models import VolunteerProfile


# Create your views here.
def VolunteerPortal(request):
    volunteer=VolunteerProfile.objects.all()
    return render(request, "Volunteers/VolunteerPortal.html",{'volunteer':volunteer})

def volunteertasks(request):
    return render(request, "Volunteers/volunteerTasks.html",context={})