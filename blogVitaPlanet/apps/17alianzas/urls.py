
from django.urls import path
from . import views

app_name = '17alianzas'

urlpatterns = [

    path('AlianzasParaLograrLosOjetivos/', views.AlianzasParaLograrLosOjetivos, name = 'Alianzas para Lograr los Ojetivos')

]
