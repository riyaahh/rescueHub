from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',context={})
def contact(request):
    return render(request, 'contact.html',context={})
def contact(request):
    return render(request,'mission.html',context={})
