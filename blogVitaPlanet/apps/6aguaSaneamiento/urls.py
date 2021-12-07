
from django.urls import path
from . import views

app_name = '6aguaSaneamiento'

urlpatterns = [

    path('AguaLimpiaYSaneamiento/', views.AguaLimpiaYSaneamiento, name = 'Agua Limpia y Saneamiento')


]
