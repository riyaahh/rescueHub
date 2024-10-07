from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import VolunteerProfile, OrganisationProfile,ReliefCampProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):
    return render(request, 'index.html',context={})
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
        vol_image=request.POST.get('vol_image')

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
        camp_image=request.POST.get('camp_image')

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
        

