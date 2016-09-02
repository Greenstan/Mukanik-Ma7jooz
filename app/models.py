from django.db import models
from datetime import datetime
from django.utils import timezone 
from django.core.mail import send_mail
from django.utils.http import urlquote 
from django.core.validators import RegexValidator

# Create your models here.

class location_model(models.Models):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=400, null=True, blank=True)
    longitude = models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True) 


