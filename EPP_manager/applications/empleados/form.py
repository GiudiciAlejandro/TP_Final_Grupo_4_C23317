from django import forms
from datetime import date, timedelta, datetime
from .models import Worker, Countries, Company, Doc_types, Certification
from django import forms


class Employee_form(forms.ModelForm):
    
    class Meta:
        model=Worker
        fields="__all__"
        widgets = {'worker_birthday' : forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'type': 'date'}),
                    'worker_comments' : forms.Textarea(
                    attrs={'rows': 5, "cols": 120, 'style': 'resize:none;'}),
                    'worker_certifications':forms.CheckboxSelectMultiple()
        }
    def clean_worker_birthday(self):
        nacimiento = self.cleaned_data['worker_birthday']
        edad = ((date.today() - nacimiento).days)/365.2425
        if edad < 18:
            raise forms.ValidationError(
                "La persona tiene menos de 18 años, esto el ilegal.")
        return nacimiento

    def clean_worker_name(self):
        nombre = self.cleaned_data['worker_name']
        if len(nombre) < 2:
            raise forms.ValidationError(
                "El nombre debe tener al menos 2 caracteres.")
        return nombre

    def clean_worker_surname(self):
        apellido = self.cleaned_data['worker_surname']
        if len(apellido) < 2:
            raise forms.ValidationError(
                "El apellido debe tener al menos 2 caracteres.")
        return apellido


class Company_form(forms.Form):
    name = forms.CharField(label="Nombre", min_length=2, required=True)
    description = forms.CharField(
        label="Descripción de la empresa", required=False)
    address = forms.CharField(label="Dirección", required=False)

    def clean_name(self):
        nombre = self.cleaned_data['name']
        if len(nombre) < 2:
            raise forms.ValidationError(
                "El nombre debe tener al menos 2 caracteres.")
        return nombre


class Certification_form(forms.Form):
    class Meta:
        model = Certification
        fields = "__all__"