
from django.urls import path
from . import views

app_name = '12produccionConsumos'

urlpatterns = [

    path('ProduccionYConsumoResponsable/', views.ProduccionYConsumoResponsable, name = 'Produccion y Consumo Responsable')

]
