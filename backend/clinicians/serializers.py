from rest_framework import serializers

from clinicians.models import Clinician


class ClinicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinician
        fields = ['first_name', 'last_name', 'national_provider_identifier']
