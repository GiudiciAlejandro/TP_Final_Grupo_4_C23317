from django import forms
from datetime import date, timedelta, datetime
from .models import Worker, Countries, Company, Doc_types



class Employee_form(forms.Form):
    name = forms.CharField(label="Nombre", min_length=2, required=True)
    surname = forms.CharField(label="Apellido", min_length=2, required=True)
    document_type= forms.ModelChoiceField(label="Tipo de documento",queryset=Doc_types.objects.all())
    document_N = forms.CharField(label="Documento", min_length=6, max_length=15, required=True)
    nacionality = forms.ModelChoiceField(label="Nacionalidad", queryset=Countries.objects.all(), widget= forms.Select(attrs={'class':'form-control'}), required=True )
    birthday = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={"type": "date"}))
    company = forms.ModelChoiceField( label="Empresa", queryset=Company.objects.all(), widget= forms.Select(attrs={'class':'form-control'}), required=True)
    email = forms.EmailField(label="email")
    comments = forms.CharField(label="Comentarios",widget=forms.Textarea(attrs={"rows":5, "cols":100, 'style':'resize:none;'}), required=False)

    def clean_birthday(self):
        nacimiento=self.cleaned_data['birthday']
        edad = ((date.today() - nacimiento).days)/365.2425
        if edad < 18:
            raise forms.ValidationError("La persona tiene menos de 18 años, esto el ilegal.")
        return nacimiento


