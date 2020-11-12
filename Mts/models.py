from django.db import models

# Create your models 
class Health(models.Model):
    username = models.CharField(max_length=50)
    patientname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    sym = models.CharField(max_length=50)

    def __str__(self):
        return self.username


