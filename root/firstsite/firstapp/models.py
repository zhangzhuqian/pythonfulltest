from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True, blake=True, max_length=200)
    job = models.CharField(null=True, blake=True, max_length=200)
