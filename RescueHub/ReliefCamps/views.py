from django.shortcuts import render, redirect
from AidTogether.models import ReliefCampProfile
from ReliefCamps.models import  ResourceRequest
from django.contrib.auth.decorators import login_required 


def CampPortal(request):
    camp=ReliefCampProfile.objects.all()
    return render(request,"ReliefCamps/CampPortal.html",context={'camp':camp})

def RequestForm(request):
    return render(request, 'ReliefCamps/RequestForm.html',context={})

@login_required
def Resource_Request(request):
    if request.method == "POST":
        requester_name = request.POST.get("name")
        requester_phone= request.POST.get("phone")
        resource_type = request.POST.get("resource_type")
        quantity= request.POST.get("quantity")
        request_details= request.POST.get("reason")
        delivery_address= request.POST.get("address")
        requested_by_date = request.POST.get("date")
        urgency_level = request.POST.get("urgency")
        status = False
        
        camp =  ReliefCampProfile.objects.get(user=request.user)


        print("Resource Type:", resource_type)
        data =  ResourceRequest(camp=camp,
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


@login_required
def ViewRequest(request):
    camp_profile = ReliefCampProfile.objects.get(user=request.user)
    # Fetch only the resource requests corresponding to the logged-in camp
    camp_requests = ResourceRequest.objects.filter(camp=camp_profile)

    return render(request, 'ReliefCamps/CampRequests.html', {'requests': camp_requests})
