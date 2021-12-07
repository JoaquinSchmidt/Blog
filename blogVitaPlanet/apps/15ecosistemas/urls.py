
from django.urls import path
from . import views

app_name = '15ecosistemas'

urlpatterns = [

    path('VidaDeEcosistemasTerrestres/', views.VidaDeEcosistemasTerrestres, name = 'Vida de Ecosistemas Terrestres')

]
