from django.shortcuts import render
from rest_framework import viewsets

from availabilities.models import Availability
from availabilities.serializers import AvailabilitySerializer


class AvailabilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clinicians to be viewed or edited.
    """

    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
