from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import patient, dossierPatient, service
from django.template import loader

# Create your views here.

def index(request):
    all_patients = patient.objects.all()    
    context = {'all_patients' : all_patients}
    return render(request , 'patient/index.html', context)


def detailPatient(request, patient_id):
    try:
        Patient = patient.objects.get(patientID = patient_id)        
    except patient.DoesNotExist:
        raise Http404('Patient does Not Exist')    
    return render(request , 'patient/detail.html', {'Patient' : Patient} )

    