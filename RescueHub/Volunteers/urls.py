from django.urls import path,include

from .import views

urlpatterns=[
    path('VolunteerPortal',views.VolunteerPortal,name="VolunteerPortal"),
    path('cardView',views.card,name="cardView"),
    path('volunteertasks', views.volunteertasks, name="volunteertasks"),
    path('denyTask/<int:id>', views.denyTask, name="denyTask"), 
    path('card',views.card,name="card"),
    path('acceptTask/<int:request_id>', views.volunteer_accept_request, name='volunteer_accept_request'),
]
