from django.db import models

class Packages(models.Model):
    SERVICE_PROVIDER = [
        ('DG', 'dialog'),
        ('MT', 'mobitel'),
        ('HT', 'hutch'),
        ('AT', 'airtel')
    ]

    PAYMENT_METHOD = [
        ('PR', 'prepaid'),
        ('PO', 'postpaid')
    ]

    PACKAGE_TYPE = [
        ('VC', 'voice'),
        ('DT', 'data'),
        ('UN', 'unlimited'),
        ('AT', 'anytime'),
        ('TB', 'time-based'),
        ('CB', 'content-based'),
        ('HB', 'home-broadband'),
        ('TV', 'television')
    ]

    service_provider = models.CharField(max_length=2, choices=SERVICE_PROVIDER)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD )
    package_type = models.CharField(max_length=2, choices=PACKAGE_TYPE)
    package_name = models.CharField(max_length=255)
    value = models.IntegerField()
    description = models.CharField(max_length=255)
    activation_method = models.CharField(max_length=255)