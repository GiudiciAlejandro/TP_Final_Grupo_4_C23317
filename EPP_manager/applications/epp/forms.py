from django import forms
from datetime import date, timedelta, datetime
from django.core.exceptions import ValidationError
from .models import *




choises_days = [tuple([x,x]) for x in range(15,365)]

class New_epp(forms.ModelForm):
    class Meta:
        model = Epp
        #fields = "__all__"
        fields= ["epp_type",
                "epp_serial_n",
                "epp_manufacturer", 
                "epp_expire_date", 
                "epp_assigned"]
        widgets = {
                    'expired_date': forms.DateInput(
                    format=('%Y-%m-%d'),
                    attrs={'type': 'date'}),
}   
    # Validaciones
    def clean_expired_dated(self):
        expired_d = self.cleaned_data['expired_dated']
        hoy = date.today()
        time_expire = ((expired_d - hoy).days)
        if time_expire < 180:
            raise forms.ValidationError(message="La fecha de validez del EPP debe ser mayor a 6 meses.")
        return time_expire


class New_epptype(forms.ModelForm):
    class Meta:
        model=Epp_types
        fields = "__all__"

    def clean_inspection_period(self):
        insp_period = self.cleaned_data['inspection_period']
        if insp_period < 15:
            raise forms.ValidationError('El período de inspección debe ser mayor a los 15 días')
        return insp_period



class New_insp(forms.ModelForm):

    class Meta:
        model=Epp_inspections
        insp_status = [("REJECTED","Rechazado"),
                        ("ACEPTED","Aceptado")]
        fields= ["epp_insp_status", "epp_insp_comments" ,"epp_inps_epp"]
        widgets = {
                    'epp_insp_status':forms.Select(
                        choices=insp_status
                    ,attrs={'class': 'form-control'}),
                    'epp_insp_comments':forms.Textarea(
                    attrs={"rows": 5, "cols": 100, 'style': 'resize:none;'}),
                    'epp_inps_epp':forms.TextInput(attrs={'readonly':'readonly'})
                    }   

