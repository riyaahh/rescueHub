from django.urls import path,include

from .import views

urlpatterns=[
    path('VolunteerPortal',views.VolunteerPortal,name="VolunteerPortal"),
    path('volunteerTasks',views.volunteerTask,name="volunteerTasks"),
]
