from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=225)
    collegeName = models.CharField(max_length=225)
    events = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)
    link = models.CharField(max_length=100)
