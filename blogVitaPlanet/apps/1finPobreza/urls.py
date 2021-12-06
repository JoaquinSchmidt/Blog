from django.urls import path
from . import views

app_name = '1finPobreza'

urlpatterns = [
    
    path('FinDeLaPobreza/', views.FinDeLaPobreza, name = 'fin_Pobreza.html'),

]
