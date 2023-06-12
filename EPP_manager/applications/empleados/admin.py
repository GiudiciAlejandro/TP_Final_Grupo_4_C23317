from django.contrib import admin
from .models import Countries, Doc_types, Company, Worker, Certification

admin.site.register(Countries)
admin.site.register(Doc_types)
admin.site.register(Company)
admin.site.register(Worker)
admin.site.register(Certification)
