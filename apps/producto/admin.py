from django.contrib import admin
from apps.producto.models import Refrigeracion, Producto, TipoProducto, LoteProduccion

# Register your models here.

class productoRegistrado(admin.ModelAdmin):
	list_display = ["__str__","precio","porcentaje_descuento","cantidad_descuento","stock","tipo"]
	list_filter = ["nombre"]
	search_fields = ["__str__","precio"]

	class Meta:
		model = Producto

class loteRegistrado(admin.ModelAdmin):
	list_display = ["__str__","fecha_produccion","fecha_vencimiento","cantidad","producto"]

admin.site.register(Refrigeracion)
admin.site.register(TipoProducto)
admin.site.register(Producto, productoRegistrado)
admin.site.register(LoteProduccion, loteRegistrado)