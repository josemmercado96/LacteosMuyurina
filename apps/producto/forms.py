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