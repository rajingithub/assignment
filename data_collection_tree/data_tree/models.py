from django.db import models

# Create your models here.

class Datatree(models.Model):
    device=models.TextField(null=True, blank=True)
    country=models.TextField(null=True, blank=True)
    webreq=models.IntegerField(null=True, blank=True)
    timespent=models.IntegerField(null=True, blank=True)