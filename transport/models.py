from django.db import models
from django.db.models.deletion import CASCADE

class Schedules(models.Model):
  mode = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  arrival = models.DateTimeField()
  
