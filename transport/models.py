from django.db import models
from django.db.models.deletion import CASCADE

class Vehical_Types(models.Model):
  type_id = models.AutoField(primary_key=True)
  vehical_type = models.CharField(max_length=20, null=False)

class Schedules(models.Model):
  trip_id = models.AutoField(primary_key=True)
  type_id = models.ForeignKey(Vehical_Types, on_delete=CASCADE, null=False)
  vehical_number = models.CharField(max_length=20, null=False)
  departure = models.CharField(max_length=20, null=False)
  dep_time = models.TimeField(null=False)
  destination = models.CharField(max_length=20, null=False)
  des_time = models.TimeField(null=False)
  booking_available = models.BooleanField(default=False, null=False)
  seats_available = models.IntegerField(null=True)

class Bookings(models.Model):
  booking_id = models.AutoField(primary_key=True)
  trip_id = models.ForeignKey(Schedules, on_delete=CASCADE, null=False)
  user_name = models.CharField(max_length=100, null=False)
  seats = models.IntegerField(null=False)

class Offices(models.Model):
  office_id = models.AutoField(primary_key=True)
  type_id = models.ForeignKey(Vehical_Types, on_delete=CASCADE, null=False)
  office_name = models.CharField(max_length=100, null=False)
  address = models.CharField(max_length=100, null=False)
  contact_number = models.CharField(max_length=20, null=True)
  email = models.EmailField(null=True)

class Complaints(models.Model):
  complaint_id = models.AutoField(primary_key=True)
  type_id = models.ForeignKey(Vehical_Types, on_delete=CASCADE, null=False)
  date = models.DateField(auto_now_add=True)
  time = models.TimeField(auto_now_add=True)
  title = models.CharField(max_length=50, null=False)
  description = models.CharField(max_length=100, null=True)
  vehical_number = models.CharField(max_length=10, null=False) 
  driver_id = models.CharField(max_length=20, null=True)
  conductor_id = models.CharField(max_length=20, null=True) 