from django import forms
from .models import Refrigeracion, TipoProducto, Producto

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