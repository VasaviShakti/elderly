from django.db import models

# Create your models 
class Health(models.Model):
    username = models.CharField(max_length=50)
    usergender = models.CharField(max_length=10)
    userage = models.CharField(max_length=10)
    patientname = models.CharField(max_length=50)
    patientgender = models.CharField(max_length=10)
    patientage = models.CharField(max_length=10)
    sym = models.CharField(max_length=50)

    def __str__(self):
        pass


