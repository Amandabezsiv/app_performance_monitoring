from django.db import models

from djongo import models

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
# Create your models here.
