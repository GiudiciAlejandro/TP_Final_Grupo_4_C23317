from django.contrib import admin
from .models import Countries, Doc_types, Company, Worker

admin.site.register(Countries)
admin.site.register(Doc_types)
admin.site.register(Company)
admin.site.register(Worker)
