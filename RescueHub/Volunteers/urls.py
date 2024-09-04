<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [

]
=======
from django.urls import path,include

from .import views

urlpatterns=[
    path('VolunteerPortal',views.VolunteerPortal,name="VolunteerPortal"),
    path('volunteertasks',views.volunteertasks,name="volunteertasks"),
]
>>>>>>> 42665a3deb48b0701cee9444e1e1307d34efa453
