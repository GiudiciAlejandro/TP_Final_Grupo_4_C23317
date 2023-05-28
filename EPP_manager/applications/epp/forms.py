from django import forms
from datetime import date, timedelta, datetime
from django.core.exceptions import ValidationError
from .models import *




choises_days = [tuple([x,x]) for x in range(15,365)]

class New_epp(forms.ModelForm):
    class Meta:
        model = Epp
        fields = "__all__"
        widgets = {'expired_date':forms.DateInput(attrs={"type": "date"})}
            
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
