from django.urls import path,include

from .import views

urlpatterns = [
    path('CampPortal.html',views.CampPortal, name="CampPortal"),
]
