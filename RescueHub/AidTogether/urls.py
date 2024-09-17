
from django.urls import path,include

from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('user_login',views.user_login,name="user_login"),
    path('home',views.index,name="home"),
    path('registration',views.registration,name="registration"),
    path('vregister', views.register_volunteer,name="vregister"),
    path('oregister', views.register_org,name="oregister"),
    path('rregister', views.register_reliefcamp,name="rregister"),
    path('login_access', views.login_access,name="login_access"),
    

]