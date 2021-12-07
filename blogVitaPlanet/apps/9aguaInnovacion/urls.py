
from django.urls import path
from . import views

app_name = '9aguaInnovacion'

urlpatterns = [

    path('IndustriaInnovacionEInfraestructura/', views.IndustriaInnovacionEInfraestructura, name = 'Industria Innovacion e Infraestructura')

]
