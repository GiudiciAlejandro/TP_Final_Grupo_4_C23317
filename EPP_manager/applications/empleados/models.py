from django.db import models


# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(verbose_name="Nombre del país", max_length=75 )
    
    def __str__(self):
        return self.country_name

class Doc_types(models.Model):
    doc_type_name=models.CharField(verbose_name="Tipo de documento", max_length=50)

    def __str__(self):
        return self.doc_type_name

class Company(models.Model):
    company_name=models.CharField(verbose_name="Compañia", max_length=25)
    company_descript = models.TextField(verbose_name="Descripción", max_length=250, null=True, blank=True)
    company_address=models.CharField(verbose_name="Dirección", max_length=250, null=True, blank=True)

    def __str__(self):
        return self.company_name

class Worker(models.Model):
    worker_name = models.CharField(verbose_name="Nombre", max_length=50,)
    worker_surname = models.CharField(verbose_name="Apellido", max_length=50,)
    worker_company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Empresa")
    worker_nationality = models.ForeignKey(Countries,on_delete=models.DO_NOTHING, verbose_name="Nacionalidad")
    worker_doc_type = models.ForeignKey(Doc_types,on_delete=models.DO_NOTHING, verbose_name="Tipo de documento")
    worker_doc_n = models.CharField(verbose_name="N° de documento", max_length=50,)
    worker_state = models.BooleanField(verbose_name="Estado")
    worker_email= models.EmailField(verbose_name="email", null=True, blank=True)
    worker_birthday = models.DateField(verbose_name="Fecha de nacimiento", default='1900-01-01')
    worker_comments = models.TextField(verbose_name="Comentarios", max_length=500, null=True, blank=True)
    def __str__(self):
        return (self.worker_surname + ", " + self.worker_name)

