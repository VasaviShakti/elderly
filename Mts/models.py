from django.db import models

# Create your models 
class Health(models.Model):
    name = models.CharField(max_length=50)
    patientname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    sympo = models.CharField(max_length=50)
    hb = models.CharField(max_length=10)
    sbp = models.CharField(max_length=10)
    dbp = models.CharField(max_length=10)
    def __str__(self):
        return self.username


