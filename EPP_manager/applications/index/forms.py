from django import forms    

class logeo(forms.Form):
    usuario=forms.CharField(label="Usuario", required= True)
    password=forms.CharField(label="Password", required= True)
