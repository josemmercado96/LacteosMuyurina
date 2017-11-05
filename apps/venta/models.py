from django.db import models
from apps.producto.models import Producto
# Create your models here.

class Cliente(models.Model):
	nit = models.CharField(max_length = 15)
	razon_social = models.CharField(max_length=80)
	telefono = models.CharField(max_length=15)
	correo = models.EmailField()
	direccion = models.TextField()

	def __str__(self):
		return self.razon_social

class Venta(models.Model):
	fecha = models.DateField()
	monto_total = models.FloatField()
	cliente = models.ForeignKey(Cliente, blank = True, null = True)

	def __str__(self):
		return self.id


class DetalleVenta(models.Model):
	cantidad = models.IntegerField()
	precio_unitario = models.FloatField()
	subtotal = models.FloatField()
	producto = models.ForeignKey(Producto)
	venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

	def __str__(self):
		return self.id
