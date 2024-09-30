from django.shortcuts import render

def CampPortal(request):
    return render(request,"ReliefCamps/CampPortal.html",context={})
def RequestForm(request):
    return render(request,"ReliefCamps/RequestForm.html",context={})
