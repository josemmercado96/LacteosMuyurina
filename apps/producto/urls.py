from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import crearRefrigeracion, listaRefrigeracion, crearTipo, listaTipos

urlpatterns = [
    url(r'^crear-refrigeracion/',login_required(crearRefrigeracion),name='refrigeracion'),
    url(r'^lista-refrigeracion/',login_required(listaRefrigeracion),name='listaRefrigeracion'),
    url(r'^crear-tipo/',login_required(crearTipo),name='crearTipo'),
    url(r'^lista-tipos/',login_required(listaTipos),name='listaTipos'),
]