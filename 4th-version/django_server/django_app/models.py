# django_app/models.py
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=8)
    address = models.CharField(max_length=255)
    age = models.IntegerField()