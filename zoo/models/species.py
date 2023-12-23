from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    CONSERVATION_STATUS = [
        ('EN', 'Endangered'),
        ('VU', 'Vulnerable'),
        ('LC', 'Least Concern'),
    ]
    conservation_status = models.CharField(max_length=2, choices=CONSERVATION_STATUS)

    class Meta:
        verbose_name_plural = "Species"

    def __str__(self):
        conservation_status_label = dict(self.CONSERVATION_STATUS).get(self.conservation_status, '')
        return f"{self.name} - {conservation_status_label}"
