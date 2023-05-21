from django import forms
from datetime import date, timedelta, datetime
from django.core.exceptions import ValidationError
from .models import *



epp_types = [('casco','Casco'), 
                ('zapatos','Zapatos'),
                ('anteojos','Anteojos'),
                ('auditivo','Protector auditivo'),
                ('guantes','Guantes'),
                ('anteojos','Anteojos'),
                ('mascarilla','Mascarilla'),
                ('chaleco','Chaleco reflectivo'),
                ]


epp_sub_types=[('none','---------------'), 
                ('casco_tipo1','Casco tipo1'), 
                ('casco_tipo2','Casco tipo2'), 
                ('casco_tipo3','Casco tipo3'), 
                ]

choises_days = [tuple([x,x]) for x in range(15,365)]

class New_epp(forms.ModelForm):
    
    class Meta:
        model = Epp
        fields = "__all__"

    # TODO ver como cambiar el tipo de input para la fecha de vencimientos
    # Validaciones
   
    def clean_expired_dated(self):
        expired_d = self.cleaned_data['expired_dated']
        hoy = date.today()
        time_expire = ((expired_d - hoy).days)
        if time_expire < 180:
            raise forms.ValidationError(message="La fecha de validez del EPP debe ser mayor a 6 meses.")
        return time_expire

    def clean_inspection_period(self):
        insp_period = self.cleaned_data['inspection_period']
        if insp_period < 15:
            raise forms.ValidationError('El período de inspección debe ser mayor a los 15 días')


class New_epptype(forms.ModelForm):
    class Meta:
        model=Epp_types
        fields = "__all__"