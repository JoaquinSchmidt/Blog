
from django.urls import path
from . import views

app_name = '3saludBienestar'

urlpatterns = [

    path('SaludyBienestar/', views.SaludYBienestar, name = 'Salud y Bienestar')


]
