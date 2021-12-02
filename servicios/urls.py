#urls de la app. 
#fue borrado el urlpattern admin, el mismo va en el urls.py del proyecto general.
from django.urls import path
# from ProyectoWebApp import views ------>
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.servicios, name="Servicios"),

]

