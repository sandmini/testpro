from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    uptime = models.IntegerField(default=0)