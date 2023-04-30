from django import forms    

class logeo(forms.Form):
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
