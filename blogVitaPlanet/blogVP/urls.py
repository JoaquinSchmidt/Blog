"""blogVP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    #path('admin/', admin.site.urls), 
    path('', views.Inicio, name = 'inicio'),
    #APPS
    path('local/', include('apps.1finPobreza.urls')),
    path('local/', include('apps.2hambreCero.urls')),
    path('local/', include('apps.3saludBienestar.urls')),
    path('local/', include('apps.4educacionDeCalidad.urls')),
    path('local/', include('apps.5igualdadGenero.urls')),
    path('local/', include('apps.6aguaSaneamiento.urls')),
    path('local/', include('apps.7energiaAsequible.urls')),
    path('local/', include('apps.8trabajoDecente.urls')),
    path('local/', include('apps.9aguaInnovacion.urls')),
    path('local/', include('apps.10reduccion.urls')),
    path('local/', include('apps.11ciudadesComunidades.urls')),
    path('local/', include('apps.12produccionConsumos.urls')),
    path('local/', include('apps.13accionClima.urls')),
    path('local/', include('apps.14vidaSubmarina.urls')),
    path('local/', include('apps.15ecosistemas.urls')),
    path('local/', include('apps.16pazJusticia.urls')),
    path('local/', include('apps.17alianzas.urls')),

]
