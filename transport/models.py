from django.db import models
from django.db.models.deletion import CASCADE

class Schedules(models.Model):
  vehical_number = models.CharField(max_length=10, null=True)
  vehical_type = models.CharField(max_length=20, null=True)
  departure = models.CharField(max_length=20)
  dep_time = models.CharField(max_length=20)
  destination = models.CharField(max_length=20)
  des_time = models.CharField(max_length=20)
  booking_available = models.CharField(max_length=10, null=True)
  seats_available = models.PositiveSmallIntegerField(null=True)
