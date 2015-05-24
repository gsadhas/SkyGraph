# Create your models here.

from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Userbkp(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Uname = models.CharField(max_length=20)
    City = models.CharField(max_length=20)

