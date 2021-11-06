import logging

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import routers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers



from .models import Appointment, Doctor, DoctorAvailability, DoctorHospitalMembership, Hospital, Patient
from .serializers import AppointmentFullSerializer, AppointmentSerializer, DoctorAvailabilityFullSerializer, DoctorAvailabilitySerializer, DoctorHospitalMembershipFullSerializer, DoctorHospitalMembershipSerializer, DoctorSerializer, HospitalSerializer, PatientSerializer

logger = logging.getLogger(__name__)

# ViewSets define the view behavior.
# https://www.django-rest-framework.org/api-guide/viewsets/#viewsets


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorHospitalMembershipViewSet(viewsets.ModelViewSet):
    queryset = DoctorHospitalMembership.objects.all()
    serializer_class = DoctorHospitalMembershipSerializer
            
    @action(detail=False, methods=["get"])
    def details(self, request):
        queryset = DoctorHospitalMembership.objects.all()
        serializer = DoctorHospitalMembershipFullSerializer(queryset, many=True)
        return Response(serializer.data)
        
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer

    @action(detail=False, methods=["get"])
    def details(self, request):
        queryset = DoctorAvailability.objects.all()
        serializer = DoctorAvailabilityFullSerializer(queryset, many=True)
        return Response(serializer.data)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # Can be later modified for any modification on the existing appointment
    # @action(detail=False, methods=["patch"])
    # def book(self, request, pk=None):
    #     appointment = Appointment.objects.get(pk=pk)
    #     patient = Patient.objects.get(pk=request.data.get("patient_pk"))
    #     logger.info("Booking appointment %s for patient %s", appointment.pk, patient.pk)
    #     # TODO: implement appointment booking logic
    #     serializer = AppointmentSerializer(appointment)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def details(self, request):
        queryset = Appointment.objects.all()
        serializer = AppointmentFullSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def book(self, request, pk=None):
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        