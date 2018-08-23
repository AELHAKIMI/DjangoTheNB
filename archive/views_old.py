from django.shortcuts import render
from django.http import HttpResponse
from .models import patient, dossierPatient, service
from django.template import loader

# Create your views here.

def index(request):
    all_patients = patient.objects.all()
    html = ''
    for Patient in all_patients:
        url = '/archive/'+ str(Patient.patientID)+ '/'
        html+= '<a href="' + url+ '">' + Patient.patientName + '</a> <br />'
    return HttpResponse(html)

def detailPatient(request, patient_id):
    return HttpResponse('<h2> datils for Patient Id : '+ str(patient_id) + '</h2>')
    