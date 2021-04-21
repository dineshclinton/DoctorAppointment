from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'clinicians', views.ClinicianViewSet)
router.register(r"appointments", views.AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
