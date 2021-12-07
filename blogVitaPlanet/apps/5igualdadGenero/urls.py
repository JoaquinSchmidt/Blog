
from django.urls import path
from . import views

app_name = '5igualdadGenero'

urlpatterns = [

    path('IgualdadDeGenero/', views.IgualdadDeGenero, name = 'Igualdad de Genero')


]
