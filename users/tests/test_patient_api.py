from django.urls import reverse
from pytest import mark
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import CustomUser
from .factories import PatientFactory, CustomUserFactory


@mark.django_db
class UserViewSetTest(APITestCase):
    def setUp(self):
        self.url: str = reverse("patient-list")

    def test_patients(self):
        user = CustomUserFactory(role="doctor")
        users = [PatientFactory() for _ in range(10)]
        self.client.force_login(user)
        with self.assertNumQueries(4):
            res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_json = res.json()
        self.assertEqual(res_json["count"], len(users))


    def test_patient_as_non_doctor(self):
        user = CustomUserFactory(role="patient")
        self.client.force_login(user)
        with self.assertNumQueries(2):
            res = self.client.get(self.url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
