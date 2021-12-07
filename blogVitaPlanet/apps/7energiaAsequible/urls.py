
from django.urls import path
from . import views

app_name = '7energiaAsequible'

urlpatterns = [

    path('EnergiaAsequibleYNoContaminante/', views.EnergiaAsequibleYNoContaminante, name = 'Energia Asequible y no Contaminante')

]
