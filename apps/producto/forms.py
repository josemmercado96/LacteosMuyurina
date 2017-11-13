from django import forms
from .models import Refrigeracion, TipoProducto

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