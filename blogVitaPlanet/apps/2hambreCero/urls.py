
from django.urls import path
from . import views

app_name = '2hambreCero'

urlpatterns = [

    path('HambreCero/', views.HambreCero, name = 'Hambre Cero')

]
