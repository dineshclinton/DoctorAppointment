from django.contrib import admin

from .models import Availability


class AvailabilityAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Availabilities"


admin.site.register(Availability, AvailabilityAdmin)
