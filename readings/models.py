from django.db import models
from django.conf import settings

# Create your models here.

class Reading(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.CharField(max_length=250)
    serial_number = models.CharField(max_length=250)
    device_timestamp = models.DateTimeField(null=True)
    recording_type = models.CharField(max_length=250)
    glucose_value_history = models.CharField(max_length=250, null=True, blank=True)
    glucose_scan = models.CharField(max_length=250, null=True, blank=True)
    
    class Meta:
       ordering = ['-id']