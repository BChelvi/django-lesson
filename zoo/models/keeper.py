from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL


class Keeper(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    hire_date = models.DateField()

    user = models.OneToOneField(User, related_name='keeper', on_delete=SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.name} - {self.hire_date}"
