from django import forms    

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
        widget=forms.TextInput(
            attrs={
                'id':'Index_name',
                'class': 'login_field'
            })
            ,required= True, )
    company = forms.CharField(label="Empresa", required=True)
    email = forms.EmailField(label="email")
    message = forms.CharField(label="Mensaje",widget=forms.Textarea())