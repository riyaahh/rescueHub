from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import VolunteerProfile, OrganisationProfile,ReliefCampProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')

# Create your views here.

def index(request):
    relief_camp_count = ReliefCampProfile.objects.all().count()
    organisation_count = OrganisationProfile.objects.all().count()
    volunteer_count = VolunteerProfile.objects.all().count()
    context={'volunteer_count': volunteer_count,'organisation_count':organisation_count,'relief_camp_count':relief_camp_count,
             }

    return render(request, 'index.html',context)
def home(request):
    return render(request, 'index.html',context={})
def user_login(request):
    return render(request, 'login.html',context={})
def contact(request):
    return render(request, 'contact.html',context={})
def registration(request):
    return render(request, 'registration.html',context={})
def mission(request):
    return render(request,'mission.html',context={})
def help(request):
    return render(request,'help.html',context={})
def news(request):
    return render(request,'news.html',context={})


def register_volunteer(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        vol_image=request.FILES.get('image1')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration', {'error': 'Passwords do not match'})

        # Check if email is already used
        if User.objects.filter(email=email).exists():
            return render(request, 'registration', {'error': 'Email already registered'})

        # Create the user
        user = User.objects.create(username=email, email=email, password=make_password(password.strip()))
        user.save()

        # Create volunteer profile
        VolunteerProfile.objects.create(
            user=user, 
            dob=dob, 
            phone=phone, 
            address=address, 
            full_name=full_name, 
            gender=gender,
            vol_image=vol_image,
        )

        # Log the user in after registration
        login(request, user)

        return redirect('home')  # Redirect to volunteer's dashboard

    return render(request, 'registration')

def login_access(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        # role = request.POST.get('role')
        
        # print(username, password)
        user = authenticate(username=username, password=password.strip())
        print(user)
        
        if user is not None:
            # Log the user in
            login(request, user)
            
            if VolunteerProfile.objects.filter(user=request.user).exists():
                # volunteer = VolunteerProfile.objects.get(user = request.user)
                return redirect('VolunteerPortal')
            elif OrganisationProfile.objects.filter(user=request.user).exists():
                return redirect('organisationPortal')
            elif ReliefCampProfile.objects.filter(user=request.user).exists():
                return redirect('CampPortal')
            else:
                print("Invalid user")
            
                

            # Redirect based on user type
            # if role == 'volunteer':
            #     return redirect('VolunteerPortal')
            # elif role == 'relief_camp':
            #     return redirect('CampPortal') 
            # elif role == 'organisation':
            #     return redirect('organisationPortal') 
        else:
            # Invalid credentials
            # return render(request, 'user_login', {'error': 'Invalid username or password'})
            return redirect('user_login')

    return redirect('user_login')

#organisation registration
def register_org(request):
    if request.method == 'POST':
        org_name = request.POST.get('org_name')
        contact_person = request.POST.get('contact_person')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        org_image=request.FILES.get('image')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration', {'error': 'Passwords do not match'})

        # Check if email is already used
        if User.objects.filter(email=email).exists():
            return render(request, 'registration', {'error': 'Email already registered'})

        # Create the user
        user = User.objects.create(username=email, email=email, password=make_password(password.strip()))
        user.save()

        # Create volunteer profile
        OrganisationProfile.objects.create(
            user=user,  
            phone=phone, 
            address=address, 
            org_name = org_name,
            contact_person=contact_person,
            org_image=org_image)

            # role='volunteer'  # Default role as volunteer


        # Log the user in after registration
        login(request, user)

        return redirect('home')  # Redirect to volunteer's dashboard

    return render(request, 'registration')


#relief camp registration

def register_reliefcamp(request):
    if request.method == 'POST':
        camp_name = request.POST.get('camp_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        contact_person= request.POST.get('contact_person')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        camp_image=request.FILES['image2']

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration', {'error': 'Passwords do not match'})

        # Check if email is already used
        if User.objects.filter(email=email).exists():
            return render(request, 'registration', {'error': 'Email already registered'})

        # Create the user
        user = User.objects.create(username=email, email=email, password=make_password(password.strip()))
        user.save()

        # Create volunteer profile
        ReliefCampProfile.objects.create(
            user=user, 
            phone=phone, 
            address=address, 
            camp_name=camp_name, 
           contact_person=contact_person,
           camp_image=camp_image,
        )

        # Log the user in after registration
        login(request, user)

        return redirect('home')  # Redirect to volunteer's dashboard

    return render(request, 'registration')

def logout_view(request):
    logout(request)  # This will log the user out
    return redirect('home')  # Redirect to the login page (or any other page)
        
#############

import matplotlib.pyplot as plt
from io import BytesIO
import base64

def generate_pie_chart(sizes, labels, colors):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close(fig)  # Close the figure to avoid memory issues
    return image_base64

def dashboard_view(request):
    # Fetch counts
    volunteer_count = VolunteerProfile.objects.all().count()
    relief_camp_count = ReliefCampProfile.objects.count()
    organisation_count = OrganisationProfile.objects.count()
    print(volunteer_count)
    # Debug print statements
    print("Dashboard View - Volunteer Count:", volunteer_count)
    print("Dashboard View - Relief Camp Count:", relief_camp_count)
    print("Dashboard View - Organisation Count:", organisation_count)

    # Generate pie charts (optional)
    volunteer_chart = generate_pie_chart([volunteer_count], ['Volunteers'], ['#ff9999']) if volunteer_count > 0 else None
    relief_camp_chart = generate_pie_chart([relief_camp_count], ['Relief Camps'], ['#66b3ff']) if relief_camp_count > 0 else None
    organisation_chart = generate_pie_chart([organisation_count], ['Organisations'], ['#99ff99']) if organisation_count > 0 else None

    # Pass data to the template
    context = {
        'volunteer_count': volunteer_count,
        'relief_camp_count': relief_camp_count,
        'organisation_count': organisation_count,
        'volunteer_chart': volunteer_chart,
        'relief_camp_chart': relief_camp_chart,
        'organisation_chart': organisation_chart,
    
    }

    print("Context Data:", context)  # Debug log the context

    return render(request,'index.html', context)



