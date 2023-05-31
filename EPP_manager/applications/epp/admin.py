from django.contrib import admin
from .models import Epp_types, Epp, Epp_inspections

admin.site.register(Epp_types)
admin.site.register(Epp)
admin.site.register(Epp_inspections)