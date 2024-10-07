from django.urls import path,include

from .import views

urlpatterns=[
    path('organisationPortal',views.organisationPortal, name="organisationPortal"),
    path('ReqTable',views.ReqTable, name="ReqTable"),
    
]