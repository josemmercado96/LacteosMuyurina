from django.db import models
from apps.venta.models import Cliente
# Create your models here.

class Freezer(models.Model):
	codigo = models.CharField(max_length=10)
	persona = models.ForeignKey(Cliente, null=True, blank=True)

	def __str__(self):
		return self.codigo