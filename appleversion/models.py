from django.db import models

# Create your models here.
from django.db import models

class AppleDevice(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    
    def __str__(self):
        return self.name

class AppleVersion(models.Model):
    device = models.ForeignKey(AppleDevice, on_delete=models.CASCADE, related_name='versions')
    version_name = models.CharField(max_length=50)
    version_number = models.CharField(max_length=20)
    release_date = models.DateField()
    
    def __str__(self):
        return f"{self.device.name} - {self.version_name}"