from django import forms
from django.core.exceptions import ValidationError


TOPIC_CHOICES = (
    ('Dni', 'Dni'),
    ('Pasaporte', 'Pasaporte'),
    ('otros', 'Otros'),
)

class BajaEmpleadoForm(forms.Form):

    #formulario con Widget
    Nombre = forms.CharField(
    label="Nombre", widget=forms.TextInput(
    attrs={'class' : 'form-control' }))
    
    Apellido = forms.CharField(
    label="Apellido",  widget=forms.TextInput(
    attrs={'class' : 'form-control' }), required=True,  min_length=3, max_length=50)
    
    Empresa =forms.CharField(
    label="Empresa", widget=forms.TextInput(
    attrs={'class' : 'form-control' }),  required=False)

    Nacionalidad= forms.CharField(
    label="Nacionalidad",  widget=forms.TextInput(
    attrs={'class' : 'form-control' }), required=True)

    Tipo_de_Documento=forms.ChoiceField(
    label="Tipo de Documento", widget=forms.Select(
    attrs={'class': 'form-control'}), choices=TOPIC_CHOICES)
    
    DNI = forms.IntegerField(
    label="DNI", widget=forms.NumberInput(
    attrs={'class': 'form-control'}), required=True)
    
    Nro_de_Celular=forms.IntegerField(
    label="N° de celular", widget=forms.NumberInput(
    attrs={'class': 'form-control', 'step': 'any'}), required=True)
    
    Comentarios= forms.CharField(widget=forms.Textarea(attrs={'rows' : '10', 'cols': '60','placeholder': 'Ingrese su comentario' }), required=False)
    
    #Validacion de caracteres de DNI
    def clean_DNI(self):
            dni_empleado = self.cleaned_data['DNI']
            print(dni_empleado, type(str(dni_empleado)))
            if len(str(dni_empleado)) != 8:
                 raise forms.ValidationError("Ingrese un DNI válido")
            dni_empleado = str(dni_empleado)
            return dni_empleado

  

 
   