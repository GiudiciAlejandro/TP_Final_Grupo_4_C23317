from django.db import models
from applications.empleados.models import Worker

# Create your models here.
class Epp_types(models.Model):
    epp_type_name=models.CharField(verbose_name="Nombre", max_length=50)
    epp_type_description=models.CharField(verbose_name="Descripcion", max_length=50)
    epp_type_insp_period=models.IntegerField(verbose_name="Período de inspección")
    epp_type_cretaed=models.DateTimeField(verbose_name="Creado")
    epp_type_deleted=models.DateTimeField(verbose_name="Borrado")

class Epp(models.Model):
    epp_type=models.ForeignKey(Epp_types,verbose_name="Tipo de EPP",on_delete=models.CASCADE)
    epp_serial_n=models.CharField(verbose_name="N° de serie", max_length=75)
    epp_manufacturer=models.CharField(verbose_name="Marca", max_length=50)
    epp_expire_date=models.DateField(verbose_name="Fecha de vencimiento")
    epp_assigned=models.ForeignKey(Worker, verbose_name="Empleado", on_delete=models.DO_NOTHING)
    epp_created=models.DateTimeField(verbose_name="Creado")
    epp_deleted=models.DateTimeField(verbose_name="Borrado")



class Epp_inspections(models.Model):
    epp_inps_epp=models.ForeignKey(Epp, on_delete=models.CASCADE)
    epp_insp_date=models.DateField(verbose_name="Fecha")
    epp_insp_comments=models.TextField(verbose_name="Comentarios", max_length=500)
    epp_insp_status=models.BooleanField(verbose_name="Resultado")
    epp_insp_next_insp=models.DateField(verbose_name="Proxima inspección")
    epp_inps_created=models.DateTimeField(verbose_name="Creado")
    epp_insp_deleted=models.DateTimeField(verbose_name="Borrado")
