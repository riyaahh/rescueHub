from django.urls import path,include

from .import views

urlpatterns=[
    path('VolunteerPortal',views.VolunteerPortal,name="VolunteerPortal"),
    path('volunteertasks',views.volunteertasks,name="volunteertasks"),
]