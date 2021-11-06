from django.db import models
from django.db.models.base import Model

# https://docs.djangoproject.com/en/3.2/topics/db/models/

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    ssn_id = models.IntegerField(unique=True)

class Doctor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    unique_doctor_id = models.IntegerField(unique=True)

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=200)
    unique_hospital_id = models.IntegerField(unique=True)

class DoctorHospitalMembership(models.Model):
    doctor = models.ForeignKey(
        Doctor, 
        on_delete=models.CASCADE, 
        related_name="DoctorHospitalMembership_withDoctor")
    hospital = models.ForeignKey(
        Hospital, 
        on_delete=models.CASCADE, 
        related_name="DoctorHospitalMembership_withHospital")

class DoctorAvailability(models.Model):
    doctor_hospital = models.ForeignKey(
        DoctorHospitalMembership,
        on_delete=models.CASCADE,
        related_name="DoctorAvailability_withDoctorHospital")
    start_time = models.DateTimeField(auto_now=False)    
    end_time = models.DateTimeField(auto_now=False)
    is_available = models.BooleanField(default=False)

class Appointment(models.Model):
    doctor_availability = models.ForeignKey(
        DoctorAvailability,
        on_delete=models.CASCADE
        ,related_name="Appointment_withDoctorAvailability")
    start_time = models.DateTimeField(auto_now=False)
    end_time = models.DateTimeField(auto_now=False)
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name="Appointment_forPatient")
