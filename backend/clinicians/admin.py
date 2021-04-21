from django.contrib import admin

from .models import Appointment, Clinician


class ClinicianAdmin(admin.ModelAdmin):
    pass


class AppointmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Clinician, ClinicianAdmin)
admin.site.register(Appointment, AppointmentAdmin)
