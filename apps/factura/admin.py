from django.contrib import admin
from apps.factura.models import Factura, DetalleFactura, Actividad, Autorizacion

# Register your models here.

class actividadRegistrada(admin.ModelAdmin):
	list_display = ["id","__str__"]

	class Meta:
		model = Actividad

class autorizacionRegistrada(admin.ModelAdmin):
	list_display = ["__str__","actividad"]

	class Meta:
		model = Autorizacion

class facturaRegistrada(admin.ModelAdmin):
	list_display = ["__str__","fecha_emitida","fecha_valida","venta"]

	class Meta:
		model = Factura

class detalleRegistrado(admin.ModelAdmin):
	list_display = ["__str__","subtotal","factura"]

	class Meta:
		model = DetalleFactura

admin.site.register(Factura, facturaRegistrada)
admin.site.register(DetalleFactura, detalleRegistrado)
admin.site.register(Actividad, actividadRegistrada)
admin.site.register(Autorizacion, autorizacionRegistrada)