
from django.urls import path
from . import views

app_name = '14vidaSubmarina'

urlpatterns = [

    path('VidaSubmarina/', views.VidaSubmarina, name = 'Vida Submarina')

]
