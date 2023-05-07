from django import forms    
from django.core.validators import RegexValidator

class Logeo(forms.Form):
    usuario=forms.CharField(
        label="Usuario",
        widget=forms.TextInput(
            attrs={
                'id':'Index_name',
                'class': 'login_field'
            })
            ,required= True, )
    password=forms.CharField(label="Password", 
     widget=forms.TextInput(
            attrs={
                'id':'Index_surnema',
                'class': 'login_field'
            })
            , required= True)


class Contact(forms.Form):
    name=forms.CharField(
        label="Nombre",
       max_length=20, validators=[RegexValidator(regex='^[a-zA-Z ]+$', message='El nombre solo puede contener letras y espacios')], required=True
        )
    company = forms.CharField(label="Empresa", required=True, min_length=2)
    email = forms.EmailField(label="email")
    message = forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={"rows":5, "cols":100, 'style':'resize:none;'}))



