from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    path('organisationPortal',views.organisationPortal, name="organisationPortal"),
    path('ReqTable',views.ReqTable, name="ReqTable"),
    path('denyRequest/<int:id>', views.denyRequest, name="denyRequest"),
    path('acceptRequest/<int:id>', views.acceptRequest, name="acceptRequest"),
    path('Reqportal',views.Reqportal,name='Reqportal'),
    path('cardorg',views.cardorg,name="cardorg"),
    path('task/<int:task_id>/', views.task_details, name='task_details'),
    path('accept/<int:request_id>/', views.org_accept_request, name='task_accept'),

]
