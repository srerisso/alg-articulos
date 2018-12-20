from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    # tarifa1 = forms.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        model = Articulo
        fields = ['codigo','descripcion','tarifa1']
