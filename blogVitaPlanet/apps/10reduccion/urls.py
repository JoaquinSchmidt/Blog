
from django.urls import path
from . import views

app_name = '10reduccion'

urlpatterns = [
    
    path('ReduccionDeLasDesigualdades/', views.ReduccionDeLasDesigualdades, name = 'Reduccion de las Desigualdades')

]
