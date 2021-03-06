from django import forms
from django.shortcuts import get_object_or_404
from .models import Refrigeracion, TipoProducto, Producto, LoteProduccion

class RefrigeracionForm(forms.ModelForm):
    class Meta:
        model = Refrigeracion
        fields = '__all__'

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = '__all__'

        labels = {
            'nombre' : 'Nombre',
            'descripcion': 'Descripción',
            'refrigeracion' : 'Refrigeración',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'refrigeracion' : forms.Select(attrs={'class':'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        labels = {
            'nombre':'Nombre',
            'precio': 'Precio',
            'porcentaje_descuento' : 'Porcentaje de Descuento',
            'cantidad_descuento' : 'Cantidad Mínima Para Descuento',
            'stock' : 'Stock',
            'stock_minimo' : 'Stock Mínimo',
            'tipo' : 'Tipo de Producto',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control'}),
            'porcentaje_descuento' : forms.NumberInput(attrs={'class':'form-control'}),
            'cantidad_descuento' : forms.NumberInput(attrs={'class':'form-control'}),
            'stock' : forms.NumberInput(attrs={'class':'form-control','readonly':'readonly','value':0}),
            'stock_minimo' : forms.NumberInput(attrs={'class':'form-control'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}),
        }

class LoteForm(forms.ModelForm):
    class Meta:
        model = LoteProduccion
        fields = '__all__'

        labels = {
            'codigo' : 'Código',
            'fecha_produccion' : 'Fecha de Producción',
            'fecha_vencimiento' : 'Fecha de Vencimiento',
            'cantidad' : 'Cantidad',
            'producto' : 'Producto',
        }

        widgets = {
            'codigo' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_produccion' : forms.DateInput(attrs={'class':'form-control'}),
            'fecha_vencimiento' : forms.DateInput(attrs={'class':'form-control'}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control'}),
            'producto' : forms.Select(attrs={'class':'form-control', 'id':'producto'}),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get("codigo")
        if not codigo:
            raise forms.ValidationError("Ingrese un Código Válido")
       # elif get_object_or_404(LoteProduccion, codigo=codigo):
         #   raise forms.ValidationError("Este Lote ya fue Registrado")
        return codigo
