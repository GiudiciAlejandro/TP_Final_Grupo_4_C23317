from django.db import models
from django.urls import reverse
from datetime import date, timedelta, datetime
from applications.empleados.models import Worker

# Create your models here.
class Epp_types(models.Model):
    epp_type_name=models.CharField(verbose_name="Nombre", max_length=50)
    epp_type_description=models.CharField(verbose_name="Descripcion", max_length=50)
    epp_type_insp_period=models.IntegerField(verbose_name="Período de inspección")
    def __str__(self):
        return self.epp_type_name

class Epp(models.Model):
    epp_type=models.ForeignKey(Epp_types,verbose_name="Tipo de EPP",on_delete=models.CASCADE, related_name="epp_type_related")
    epp_serial_n=models.CharField(verbose_name="N° de serie", max_length=75)
    epp_manufacturer=models.CharField(verbose_name="Marca", max_length=50)
    epp_expire_date=models.DateField(verbose_name="Fecha de vencimiento")
    epp_assigned=models.ForeignKey(Worker, verbose_name="Empleado", 
    on_delete=models.DO_NOTHING, related_name="worker_related", null=True, blank=True)
    epp_next_insp_date=models.DateField(verbose_name="Fecha proxima inspección", default='1900-01-01')

    def get_absolute_url(self):
        return reverse("epp_detail",  args=[str(self.id)])
    

class Epp_inspections(models.Model):
    epp_inps_epp=models.ForeignKey(Epp, on_delete=models.CASCADE, related_name="epp_related")
    epp_insp_date=models.DateField(verbose_name="Fecha")
    epp_insp_comments=models.TextField(verbose_name="Comentarios", max_length=500)
    epp_insp_status=models.BooleanField(verbose_name="Resultado")
    epp_insp_next_insp=models.DateField(verbose_name="Proxima inspección")
    
