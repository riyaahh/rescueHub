from django.urls import path,include

from .import views

urlpatterns = [
    path('CampPortal',views.CampPortal, name="CampPortal"),
    path('RequestForm',views.RequestForm, name="RequestForm"),
]
