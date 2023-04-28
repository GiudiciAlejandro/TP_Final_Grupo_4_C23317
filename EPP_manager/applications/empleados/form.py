from django import forms

class BajaEmpleadoForm(forms.Form):
    Nombre = forms.CharField(label="Nombre", required=True)
    Apellido = forms.CharField(label="Apellido", required=True)
    DNI = forms.IntegerField(label="DNI", required=True)