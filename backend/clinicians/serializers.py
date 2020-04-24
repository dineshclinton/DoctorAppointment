from clinicians.models import Clinician
from rest_framework import serializers

class ClinicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinician
        fields = ['first_name', 'last_name', 'national_provider_identifier']

