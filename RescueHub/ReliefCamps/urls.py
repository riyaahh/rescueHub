from django.urls import path

from .import views

urlpatterns = [
    path('CampPortal.html',views.CampPortal, name="CampPortal"),
]

