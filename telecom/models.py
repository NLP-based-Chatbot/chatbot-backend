from django.db import models

class Packages(models.Model):
    service_provider = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    package_type = models.CharField(max_length=20)
    package_name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.CharField(max_length=400)
    activation_method = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

class Complaint(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class ProviderSpecificDetails(models.Model):
    detail_type = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    url = models.CharField(max_length=255)