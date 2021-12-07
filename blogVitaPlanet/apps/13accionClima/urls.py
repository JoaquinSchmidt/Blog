
from django.urls import path
from . import views

app_name = '13accionClima'

urlpatterns = [

    path('AccionPorElClima/', views.AccionPorElClima, name = 'Accion por el Clima')

]
