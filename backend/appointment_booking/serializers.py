from rest_framework import serializers

from .models import Appointment, Doctor, DoctorAvailability, Patient, Hospital, DoctorHospitalMembership
from django.db.models import Q
# Serializers define the API representation.
# https://www.django-rest-framework.org/api-guide/serializers/#serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        read_only_fields = ["pk"]
        fields = ["pk", "first_name", "last_name", "ssn_id"]

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        read_only_fields = ["pk"]
        fields = ["pk", "first_name", "last_name", "unique_doctor_id"]

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        read_only_fields = ["pk"]
        fields = ["pk", "hospital_name", "unique_hospital_id"]

class DoctorHospitalMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorHospitalMembership
        read_only_fields = ["pk"]
        fields = ["pk", "doctor", "hospital"]

class DoctorHospitalMembershipFullSerializer(serializers.Serializer):
    doctor = DoctorSerializer()
    hospital = HospitalSerializer()

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        read_only_fields = ["pk"]
        fields = ["pk", "doctor_hospital", "start_time", "end_time", "is_available"]

    def validate(self, data):
        """
        Check that start_time is before end_time.
        """
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("end_time must occur after start_time")

class DoctorAvailabilityFullSerializer(serializers.ModelSerializer):
    doctor_hospital = DoctorHospitalMembershipFullSerializer()   
    class Meta:
        model = DoctorAvailability
        read_only_fields = ["pk"]
        fields = ["pk", "doctor_hospital", "start_time", "end_time", "is_available"]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        read_only_fields = ["pk"]
        fields = ["pk", "start_time", "end_time", "patient", "doctor_availability"]
    
    def validate(self, data):
        """
        Check that start_time is before end_time.
        """
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("end_time must occur after start_time")
        
        doctorAvailability = DoctorAvailabilitySerializer(data['doctor_availability'])

        serializedData = AppointmentSerializer(data)

        concurrentAppointment = Appointment.objects.filter(doctor_availability = doctorAvailability.data['pk']).filter(Q(Q(start_time__lt=serializedData['start_time'].value) & Q(end_time__gt=serializedData['start_time'].value)) | Q(Q(start_time__lt=serializedData['end_time'].value) & Q(end_time__gt=serializedData['end_time'].value)) | Q(Q(start_time = serializedData['start_time'].value)) | Q(end_time = serializedData['end_time'].value))
        #.filter(Q(start_time__range=[serializedData['start_time'].value, serializedData['end_time'].value]) | Q(end_time__range=[serializedData['start_time'].value, serializedData['end_time'].value]))
        
        
        if concurrentAppointment.count() > 0 :
            raise serializers.ValidationError("patient appointment in this time slot is already booked, please revisit the available time slot")

        if ((doctorAvailability.data['start_time'] <= serializedData['start_time'].value) & (doctorAvailability.data['end_time'] >= serializedData['end_time'].value)) == False:
            raise serializers.ValidationError("appointments can be scheduled only between doctor available Start Time and End Time")

        if doctorAvailability.data['is_available'] == False:
            raise serializers.ValidationError("doctor is unavailable")

        return data

class AppointmentFullSerializer(serializers.ModelSerializer):
    doctor_availability = DoctorAvailabilityFullSerializer()
    patient = PatientSerializer()
    class Meta:
        model = Appointment
        read_only_fields = ["pk"]
        fields = ["pk", "start_time", "end_time", "patient", "doctor_availability"]