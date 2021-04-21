from rest_framework import serializers

from clinicians.models import Appointment, Clinician


class ClinicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clinician
        fields = ['first_name', 'last_name', 'national_provider_identifier']


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ['availability', 'clinician', 'status']
