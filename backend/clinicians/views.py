from django.shortcuts import render
from rest_framework import viewsets

from clinicians.models import Appointment, Clinician
from clinicians.serializers import AppointmentSerializer, ClinicianSerializer


class ClinicianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clinicians to be viewed or edited.
    """
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appointments to be viewed or edited.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
