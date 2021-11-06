from django.contrib import admin

from .models import Appointment, Patient, Doctor, Hospital, DoctorHospitalMembership, DoctorAvailability

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Hospital)
admin.site.register(DoctorHospitalMembership)
admin.site.register( DoctorAvailability)
admin.site.register(Appointment)
