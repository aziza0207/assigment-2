from django.db.models import TextChoices


class Role(TextChoices):
    DOCTOR = "doctor", "doctor"
    PATIENT = "patient", "patient"
