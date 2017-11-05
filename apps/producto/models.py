from django.db import models

# Create your models here.


class Refrigeracion(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre

class TipoProducto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	refrigeracion = models.ForeignKey(Refrigeracion)

	def __str__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	precio = models.FloatField()
	porcentaje_descuento = models.FloatField()
	cantidad_descuento = models.IntegerField()
	stock = models.IntegerField()
	stock_minimo = models.IntegerField()
	tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class LoteProduccion(models.Model):
	codigo = models.CharField(max_length=50)
	fecha_produccion = models.DateField()
	fecha_vencimiento = models.DateField()
	cantidad = models.IntegerField()
	producto = models.ForeignKey(Producto)

	def __str__(self):
		self.codigo

