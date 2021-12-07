
from django.urls import path
from . import views

app_name = '11ciudadesComunidades'

urlpatterns = [

    path('CiudadesYComunidadesSostenibles/', views.CiudadesYComunidadesSostenibles, name = 'Ciudades y Comunidades Sostenibles')

]
