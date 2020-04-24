from django.contrib import admin

from .models import Clinician


class ClinicianAdmin(admin.ModelAdmin):
    pass


admin.site.register(Clinician, ClinicianAdmin)
