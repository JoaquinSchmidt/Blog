
from django.urls import path
from . import views

app_name = '8trabajoDecente'

urlpatterns = [

    path('TrabajoDecenteYCrecinientoEconomico/', views.TrabajoDecenteYCrecinientoEconomico, name = 'Trabajo Decente y Creciniento Economico')

]
