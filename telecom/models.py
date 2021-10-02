from django.db import models

class Packages(models.Model):
    service_provider = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    package_type = models.CharField(max_length=20)
    package_name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.CharField(max_length=255)
    activation_method = models.CharField(max_length=255)