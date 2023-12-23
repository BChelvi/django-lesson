from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    species = models.ForeignKey('Species', on_delete=models.CASCADE, related_name='animals')
    DIET_CHOICES = [
        ('CR', 'Carnivore'),
        ('HR', 'Herbivore'),
        ('OM', 'Omnivore'),
    ]
    diet = models.CharField(max_length=2, choices=DIET_CHOICES)
    weight = models.FloatField()
    zone = models.ForeignKey('Zone', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        diet_label = dict(self.DIET_CHOICES).get(self.diet, '')
        return f"{self.name} - {self.species} - {diet_label}"
