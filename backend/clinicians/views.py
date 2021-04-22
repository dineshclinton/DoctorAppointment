from rest_framework import viewsets

from clinicians.models import Clinician
from clinicians.serializers import ClinicianSerializer


class ClinicianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clinicians to be viewed or edited.
    """
    queryset = Clinician.objects.all()
    serializer_class = ClinicianSerializer
