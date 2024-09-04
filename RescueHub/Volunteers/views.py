from django.shortcuts import render

# Create your views here.
def VolunteerPortal(request):
    return render(request, "Volunteers/VolunteerPortal.html",context={})
def volunteertasks(request):
    return render(request, "Volunteers/volunteerTasks.html",context={})