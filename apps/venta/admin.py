from django.contrib import admin
from apps.venta.models import Cliente, Venta, DetalleVenta

# Register your models here.

class clienteRegistrado(admin.ModelAdmin):
	list_display = ["__str__","nit","correo","telefono"]

	class Meta:
		model = Cliente

class ventaRegistrada(admin.ModelAdmin):
	list_display = ["__str__","fecha","monto_total","cliente"]

	class Meta:
		model = Venta

class detalleRegistrado(admin.ModelAdmin):
	list_display = ["__str__","producto","cantidad","subtotal"]

	class Meta:
		model = DetalleVenta
		
admin.site.register(Cliente, clienteRegistrado)
admin.site.register(Venta, ventaRegistrada)
admin.site.register(DetalleVenta, detalleRegistrado)