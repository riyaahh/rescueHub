
from django.urls import path,include

from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login")
]