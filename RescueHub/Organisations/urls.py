from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    path('organisationPortal',views.organisationPortal, name="organisationPortal"),
    path('ReqTable',views.ReqTable, name="ReqTable"),
<<<<<<< HEAD
]
=======
    path('denyRequest/<int:id>', views.denyRequest, name="denyRequest"),
    path('acceptRequest/<int:id>', views.acceptRequest, name="acceptRequest"),

]
>>>>>>> ede9c905eaf6ca80a8d0a64dbc3f16cfb6b3d18b
