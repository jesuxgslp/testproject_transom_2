from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from .views import *


urlpatterns = [    
    url(r'^$',home,name = "index"),
    url(r'^create_carro/',CreateCarro.as_view(),name = "create_carro"),
   
    
] 