from django.urls import path,include

from .import views

urlpatterns=[
    path('VolunteerPortal',views.VolunteerPortal,name="VolunteerPortal"),
    path('volunteerTasks',views.volunteerTasks,name="volunteerTasks"),
    path('denyTask/<int:id>', views.denyTask, name="denyTask"),
    path('acceptTask/<int:id>', views.acceptTask, name="acceptTask"),
    path('Taskrequests',views.Taskrequests,name="Taskrequests"),
    path('card',views.card,name="card"),
    
    
]
