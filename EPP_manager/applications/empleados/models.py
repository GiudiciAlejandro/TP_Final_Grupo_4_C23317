from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(verbose_name="Nombre del país", max_length=75 )

class Doc_types(models.Model):
    doc_type_name=models.CharField(verbose_name="Tipo de documento", max_length=50)

class Company(models.Model):
    company_name=models.CharField(verbose_name="Compañia", max_length=25)
    company_descript = models.TextField(verbose_name="Descripción", max_length=250)
    company_address=models.CharField(verbose_name="Dirección", max_length=250)
    company_created=models.DateTimeField(verbose_name="Creado")
    company_deleted = models.DateTimeField(verbose_name="Borrado", null=True, blank=True)

class Worker(models.Model):
    worker_name = models.CharField(verbose_name="Nombre", max_length=50,)
    worker_surname = models.CharField(verbose_name="Apellido", max_length=50,)
    worker_company = models.CharField(verbose_name="Empresa", max_length=50,)
    worker_nationality = models.ForeignKey(Countries,on_delete=models.DO_NOTHING)
    worker_doc_type = models.ForeignKey(Doc_types,on_delete=models.DO_NOTHING)
    worker_doc_n = models.CharField(verbose_name="N° de documento", max_length=50,)
    worker_state = models.BooleanField(verbose_name="Estado",)
    worker_comments = models.TextField(verbose_name="Comentarios", max_length=500,)
    worker_created = models.DateTimeField(verbose_name="Creado")
    worker_deleted = models.DateTimeField(verbose_name="Borrado", null=True, blank=True)


