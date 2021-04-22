from django.contrib import admin

from .models import Availability


class AvailabilityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Availability, AvailabilityAdmin)
