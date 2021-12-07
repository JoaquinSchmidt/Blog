
from django.urls import path
from . import views

app_name = '4educacionDeCalidad'

urlpatterns = [

    path('EducacionDeCalidad/', views.EducacionDeCalidad, name = 'Educacion de Calidad')

]
