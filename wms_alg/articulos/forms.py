from django.forms import ModelForm
from .models import Articulo

class ArticuloForm(ModelForm):
    # tarifa1 = forms.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        model = Articulo
        fields = ['tarifa1']
