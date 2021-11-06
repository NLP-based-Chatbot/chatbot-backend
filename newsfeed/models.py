from django.db import models

class News(models.Model):
    domain = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=600)
    date = models.DateField()
    img_url = models.CharField(max_length=255)

class Instruction(models.Model):
    domain = models.CharField(max_length=20)
    label = models.CharField(max_length=50)
    body = models.CharField(max_length=255)