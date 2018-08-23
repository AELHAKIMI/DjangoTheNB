from django.contrib import admin
from .models import patient, service, dossierPatient

# Register your models here.
admin.site.register(patient)
admin.site.register(service)
admin.site.register(dossierPatient)
