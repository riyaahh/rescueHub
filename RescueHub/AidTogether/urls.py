
from django.urls import path,include
import Organisations.urls
from django.conf import settings
from django.conf.urls.static import static
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

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

