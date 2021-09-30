from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_id   =   models.AutoField(primary_key=True)
    initials    =   models.CharField(max_length=10)
    first_name  =   models.CharField(max_length=30)
    last_name   =   models.CharField(max_length=30)
    docthash    =   models.CharField(max_length=40)


class Appiontment(models.Model):
    appointment_id  = models.AutoField(primary_key=True)
    doctor_id       = models.IntegerField()
    cust_id         = models.IntegerField()
    time_slot       = models.TimeField()
    date            = models.DateField()

class DoctorAvailable(models.Model):
    avbl_id     = models.AutoField(primary_key=True)
    doctor_id   = models.IntegerField()
    date        = models.DateField()
    time_from   = models.TimeField()
    time_to     = models.TimeField()


class DoctorSpec(models.Model):
    d2s_id      = models.AutoField(primary_key=True)
    doctor_id   = models.IntegerField()
    spec_id     = models.IntegerField()


class Specialization(models.Model):
    spec_id     = models.AutoField(primary_key=True)
    spec_name   = models.CharField(max_length=30)

class Patient(models.Model):
    cust_id     = models.AutoField(primary_key=True)
    username    = models.CharField(max_length=100)
    userhash    = models.CharField(max_length=40)

class Report(models.Model):
    report_id   = models.AutoField(primary_key=True)
    cust_id     = models.IntegerField()
    report_filename     = models.CharField(max_length=100)
    reporthash  = models.CharField(max_length=40)

    