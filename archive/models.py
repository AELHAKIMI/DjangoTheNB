from django.db import models

# Create your models here.

class patient(models.Model):
    patientID = models.CharField(max_length=12)
    patientName = models.CharField(max_length= 100)
    
    

    def __str__(self):
        return self.patientID + " - " + self.patientName
        

class service(models.Model):
    serviceID = models.CharField(max_length=12)
    service = models.CharField(max_length = 256)

    def __str__(self):
        return self.serviceID + " - " + self.service

class dossierPatient(models.Model):
    patientID = models.ForeignKey(patient, on_delete=models.CASCADE)
    DossierID = models.CharField(max_length= 32)
    is_active = models.BooleanField(default=False)
    serviceID = models.ForeignKey(service, on_delete=models.CASCADE)

    def __str__(self):
        return self.DossierID + " - " + str(self.patientID)


    
    