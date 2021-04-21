from availabilities.models import Availability
from django.db import models


class Clinician(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    national_provider_identifier = models.CharField(max_length=10, unique=True)
    availabilities = models.ManyToManyField(
        Availability,
        through='Appointment',
        through_fields=(
            'clinician',
            'availability'
        ),
    )


class AppointmentStatus:
    AVAILABLE = "available"
    BOOKED = "booked"


APPOINTMENT_STATUS_CHOICES = [
    (AppointmentStatus.AVAILABLE, "Available"),
    (AppointmentStatus.BOOKED, "Booked"),
]


class Appointment(models.Model):
    availability = models.ForeignKey(
        Availability,
        on_delete=models.CASCADE,
    )
    clinician = models.ForeignKey(
        Clinician,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        choices=APPOINTMENT_STATUS_CHOICES,
        max_length=10
    ) 
