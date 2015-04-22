from django.db import models

# Create your models here.


class DummyData(models.Model):
    number = models.CharField(max_length=100)
