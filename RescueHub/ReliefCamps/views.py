from django.shortcuts import render

def CampPortal(request):
    return render(request,"ReliefCamps/CampPortal.html",context={})
