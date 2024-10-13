from django.shortcuts import render,redirect
from AidTogether.models import VolunteerProfile,OrganisationProfile
from django.contrib.auth.decorators import login_required 

# Create your views here.
def VolunteerPortal(request):
    volunteer=VolunteerProfile.objects.all()
    return render(request, "Volunteers/VolunteerPortal.html",{'volunteer':volunteer})

@login_required
def volunteertasks(request):
    try:
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('login_url')  # Replace 'login_url' with your actual login URL
        
        # Attempt to retrieve the organisation profile
        org_details = OrganisationProfile.objects.get(user=request.user)
        
        # Fetch organisation requests (if applicable)
        org_request = OrganisationProfile.objects.filter(id=org_details.id)
        
    except OrganisationProfile.DoesNotExist:
        # Handle the case where the profile doesn't exist
        org_request = []
        return render(request, "Volunteers/volunteerTasks.html", {
            'requests': org_request,
            'message': 'No organisation profile found for the current user.'
        })

    return render(request, "Volunteers/volunteerTasks.html", {'requests': org_request})
