from django.db import models
from django.db.models.deletion import CASCADE

class Schedules(models.Model):
  mode = models.CharField(max_length=100)
  departure = models.CharField(max_length=100)
  dep_time = models.CharField(max_length=20)
  destination = models.CharField(max_length=100)
  des_time = models.CharField(max_length=20)
