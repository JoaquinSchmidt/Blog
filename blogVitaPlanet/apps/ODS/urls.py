from django.urls import path
from . import views

app_name = 'ODS'

urlpatterns = [
    
    path('ObjetivosDeDesarrolloSostenible/', views.ODS, name = 'ods')
   
]
