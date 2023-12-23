from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=100)
    CLIMATE_CHOICES = [
        ('TR', 'Tropical'),
        ('TE', 'Temperate'),
        ('AR', 'Arctic'),
    ]
    climate = models.CharField(max_length=2, choices=CLIMATE_CHOICES)
    area = models.IntegerField()
    keepers = models.ManyToManyField('Keeper', related_name='zones')

    def __str__(self):
        climate_label = dict(self.CLIMATE_CHOICES).get(self.climate, '')
        return f"{self.name} - {climate_label}"
