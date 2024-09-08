from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import VolunteerProfile
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

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

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'registration', {'error': 'Passwords do not match'})

        # Check if email is already used
        if User.objects.filter(email=email).exists():
            return render(request, 'registration', {'error': 'Email already registered'})

        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)

        # Create volunteer profile
        VolunteerProfile.objects.create(
            user=user, 
            dob=dob, 
            phone=phone, 
            address=address, 
            full_name=full_name, 
            gender=gender,
            role='volunteer'  # Default role as volunteer
        )

        # Log the user in after registration
        login(request, user)

        return redirect('home')  # Redirect to volunteer's dashboard

    return render(request, 'registration')

def login_access(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        user = authenticate(request, username=username, password=password, role=role)
        
        if user is not None:
            # Log the user in
            auth_login(request, user)

            # Redirect based on user type
            if role == 'volunteer':
                return redirect('VolunteerPortal')
            elif role == 'relief_camp':
                return redirect('CampPortal') 
            elif role == 'organisation':
                return redirect('organisationPortal') 
        else:
            # Invalid credentials
            return render(request, 'user_login', {'error': 'Invalid username or password'})

    return render(request, 'user_login')
        

