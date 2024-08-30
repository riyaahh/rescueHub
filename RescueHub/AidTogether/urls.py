
from django.urls import path,include

from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('mission',views.mission,name="mission"),
    path('help',views.help,name="help"),
    path('news',views.news,name="news"),
]