from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import index, crearCliente, listaCliente


urlpatterns = [
	url(r'^$',login_required(index),name='venta'),
	url(r'^crear-cliente/',login_required(crearCliente),name='cliente'),
	url(r'^lista-clientes/',login_required(listaCliente),name='listaCliente'),
]