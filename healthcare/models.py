from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_id   =   models.AutoField(primary_key=True)
    initials    =   models.CharField(max_length=10)
    first_name  =   models.CharField(max_length=30)
    last_name   =   models.CharField(max_length=30)
    docthash    =   models.CharField(max_length=40)

class Patient(models.Model):
    cust_id     = models.AutoField(primary_key=True)
    username    = models.CharField(max_length=100)
    userhash    = models.CharField(max_length=40)

class Specialization(models.Model):
    spec_id     = models.AutoField(primary_key=True)
    spec_name   = models.CharField(max_length=30)

class Report(models.Model):
    report_id   = models.AutoField(primary_key=True)
    cust_id     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_name     = models.CharField(max_length=100)
    reporthash  = models.CharField(max_length=40)
    available_on = models.DateField()

class Appiontment(models.Model):
    appointment_id  = models.AutoField(primary_key=True)
    doctor_id       = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    cust_id         = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_slot       = models.TimeField()
    date            = models.DateField()

class DoctorAvailable(models.Model):
    avbl_id     = models.AutoField(primary_key=True)
    doctor_id   = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time_from   = models.TimeField()
    time_to     = models.TimeField()

class DoctorSpec(models.Model):
    d2s_id      = models.AutoField(primary_key=True)
    doctor_id   = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    spec_id     = models.ForeignKey(Specialization, on_delete=models.CASCADE)

class MedicalTest(models.Model):
    medtest_id  = models.AutoField(primary_key=True)
    cust_id     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_slot   = models.TimeField()
    date        = models.DateField()
    test_type   = models.CharField(max_length=50)
    report_id   = models.ForeignKey(Report, on_delete=models.CASCADE)

class Complaint(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    email = models.CharField(max_length=50)