from django import forms

class ArticuloForm(forms.Form):
    tarifa1 = forms.DecimalField(max_digits=6, decimal_places=2)
