from django.shortcuts import render
from django.http import HttpResponse
from .models import patient, dossierPatient, service
from django.template import loader

# Create your views here.

def index(request):
    all_patients = patient.objects.all()
    template = loader.get_template('patient/index.html')
    context = {
        'all_patients' : all_patients,
    }
    return HttpResponse(template.render(context, request))

def detailPatient(request, patient_id):
    return HttpResponse('<h2> details for Patient Id : '+ str(patient_id) + '</h2>')
    