from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.ForeignKey(Country, related_name='regions', on_delete=CASCADE)

    def __str__(self):
        return f"{self.name} - {self.country}"


class NaturalReserve(models.Model):
    name = models.CharField(max_length=100, null=False)
    regions = models.ManyToManyField(Region, related_name='natural_reserves')
