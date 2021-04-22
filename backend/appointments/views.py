from rest_framework import viewsets

from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appointments to be viewed or edited.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
