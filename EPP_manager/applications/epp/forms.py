from django import forms    




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

class New_epp(forms.Form):
   
    epp_type = forms.ChoiceField(
         label="Tipo de EPP",
         choices=epp_types,
         required = True,)
    
    epp_sub_type =forms.ChoiceField(
         label="Subtipo de EPP",
         choices=epp_sub_types,
         required = True,)
    
    

    manufacturer = forms.CharField(label="Fabricante",
        required = True,
        )

    serial_n = forms.CharField(label="N° de serie",
        required = True,
        )

    expired_dated = forms.DateField(label="Fecha de vencimiento", widget=forms.DateInput(attrs={'type': 'date'}))

    
    inspection_period = forms.IntegerField(label="Periodo entre inspecciones (días)", widget=forms.Select(choices=choises_days))
    
    comment = forms.CharField(label="Comentarios",widget=forms.Textarea())