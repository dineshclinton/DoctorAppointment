from django.utils import timezone
from rest_framework.test import APITestCase

from .models import Appointment, Patient


class AppointmentBookingTestCase(APITestCase):
    def test_appointment_booking(self):
        appointment = Appointment.objects.create(start_time=timezone.now(), end_time=timezone.now())
        patient = Patient.objects.create()
        response = self.client.get(f"/appointments/{appointment.pk}/")
        assert response.json()["pk"] == appointment.pk
        response = self.client.patch(
            f"/appointments/{appointment.pk}/book/", {"patient_pk": patient.pk}, format="json"
        )
        assert response.status_code == 200
        assert response.data["pk"] == appointment.pk
        # TODO: test that the Appointment is now associated with the Patient

    def test_appointment_booking_test_unavailable_doctor(self):        
        response = self.client.post(
            f"/appointments/book/", {"patient": 1, "doctor_availability": 5, "start_time": "2021-11-08T08:30:00Z", "end_time": "2021-11-08T09:30:00Z"}, format="json"
        )
        assert response.status_code == 400

    def test_appointment_booking_test_available_doctor(self):        
        response = self.client.post(
            f"/appointments/book/", {"patient": 1, "doctor_availability": 5, "start_time": "2021-11-11T08:30:00Z", "end_time": "2021-11-11T09:30:00Z"}, format="json"
        )
        assert response.status_code == 200

    def test_appointment_booking_test_endtime_lt_starttime_doctor(self):        
        response = self.client.post(
            f"/appointments/book/", {"patient": 1, "doctor_availability": 5, "start_time": "2021-11-11T10:30:00Z", "end_time": "2021-11-11T09:30:00Z"}, format="json"
        )
        assert response.status_code == 400

    def test_appointment_booking_test_alreadybooked(self):        
        response = self.client.post(
            f"/appointments/book/", {"patient": 1, "doctor_availability": 1, "start_time": "2021-11-08T08:30:00Z", "end_time": "2021-11-08T09:30:00Z"}, format="json"
        )
        assert response.status_code == 400

    def test_appointment_booking_test_slotUnavailable(self):        
        response = self.client.post(
            f"/appointments/book/", {"patient": 1, "doctor_availability": 1, "start_time": "2021-11-08T20:30:00Z", "end_time": "2021-11-08T22:30:00Z"}, format="json"
        )
        assert response.status_code == 400