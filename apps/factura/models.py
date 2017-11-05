from django.db import models
from apps.venta.models import Venta
# Create your models here.

class Actividad(models.Model):
	nombre = models.CharField(max_length= 30)

	def __str__(self):
		return self.nombre

class Autorizacion(models.Model):
	nro_autorizacion = models.CharField(max_length=50)
	actividad = models.OneToOneField(Actividad)

	def __str__(self):
		return self.nro_autorizacion

class Factura(models.Model):
	numero = models.CharField(max_length=50)
	fecha_emitida = models.DateField()
	fecha_valida = models.DateField()
	venta = models.ForeignKey(Venta)
	autorizacion = models.ForeignKey(Autorizacion)

	def __str__(self):
		return self.numero

class DetalleFactura(models.Model):
	producto = models.CharField(max_length=50)
	cantidad = models.IntegerField()
	producto_unitario = models.FloatField()
	subtotal = models.FloatField()
	factura = models.ForeignKey(Factura)

	


