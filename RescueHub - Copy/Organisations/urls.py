from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    path('organisationPortal',views.organisationPortal, name="organisationPortal"),
    path('ReqTable',views.ReqTable, name="ReqTable"),
    path('denyRequest/<int:id>', views.denyRequest, name="denyRequest"),
    path('acceptRequest/<int:id>', views.acceptRequest, name="acceptRequest"),

]
