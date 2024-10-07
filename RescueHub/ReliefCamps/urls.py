from django.urls import path,include

from .import views

urlpatterns = [
    path('CampPortal',views.CampPortal, name="CampPortal"),
    path('RequestForm',views.RequestForm, name="RequestForm"),
    path('Resource_request',views.Resource_Request, name="Resource_Request"),
    # path('CampRequests',views.CampRequests, name="CampRequests"),
    path('ViewRequest',views.ViewRequest, name="ViewRequest"),
    
    
]
