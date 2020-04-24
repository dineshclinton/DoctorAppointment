from django.db import models

from availabilities.models import Availability


class Clinician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_provider_identifier = models.CharField(max_length=10, unique=True)
    availabilities = models.ManyToManyField(Availability)
