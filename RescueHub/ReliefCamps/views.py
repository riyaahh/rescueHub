from django.shortcuts import render, redirect
from AidTogether.models import ReliefCampProfile
from ReliefCamps.models import  ResourceRequest


def CampPortal(request):
    camp=ReliefCampProfile.objects.all()
    return render(request,"ReliefCamps/CampPortal.html",context={'camp':camp})

def RequestForm(request):
    return render(request, 'ReliefCamps/RequestForm.html',context={})

# def CampRequests(request):
#     return render(request, 'ReliefCamps/CampRequests.html',context={})

def Resource_Request(request):
    if request.method == "POST":
        camp_name = request.POST.get("CampName")
        camp_email = request.POST.get("CampEmail")
        camp_phone = request.POST.get("ph")
        requester_name = request.POST.get("name")
        requester_phone= request.POST.get("phone")
        resource_type = request.POST.get("resource_type")
        quantity= request.POST.get("quantity")
        request_details= request.POST.get("reason")
        delivery_address= request.POST.get("address")
        requested_by_date = request.POST.get("date")
        urgency_level = request.POST.get("urgency")
        status = False
          

        print("Resource Type:", resource_type)
        data =  ResourceRequest(camp_name=camp_name,
                                camp_email=camp_email,
                                camp_phone=camp_phone,
                                requester_name=requester_name,
                                requester_phone = requester_phone,
                                resource_type = resource_type,
                                quantity = quantity,
                                request_details  = request_details,
                                delivery_address = delivery_address,
                                requested_by_date = requested_by_date,
                                urgency_level = urgency_level,
                                status=status,
                                )
        data.save()
        return redirect('CampPortal')
        
    
    return render(request, 'ReliefCamps/RequestForm.html')

def ViewRequest(request):
    camp_email = request.user.email  # or however you are identifying the camp
    
    # Fetch only the resource requests for the logged-in camp
    camp_requests = ResourceRequest.objects.filter(camp_email=camp_email)
    # print(camp_requests)
    return render(request, 'ReliefCamps/CampRequests.html', {'requests': camp_requests})
