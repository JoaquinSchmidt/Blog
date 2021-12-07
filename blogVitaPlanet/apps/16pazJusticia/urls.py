
from django.urls import path
from . import views

app_name = '16pazJusticia'

urlpatterns = [

    path('PazJusticiaEInstitucionesSolidas/', views.PazJusticiaEInstitucionesSolidas, name = 'Paz Justicia e Instituciones Solidas')

]
