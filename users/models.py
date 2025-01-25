from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from .managers import CustomUserManager
from .constants import Role


class CustomUser(AbstractUser):
    first_name = models.CharField(_("First name"), max_length=30, blank=True)
    last_name = models.CharField(_("Last name"), max_length=30, blank=True)
    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(_("Role"), choices=Role.choices, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="patient"
    )
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"))
    diagnoses = ArrayField(
        ArrayField(models.CharField(max_length=200)), blank=True, null=True, verbose_name="Diagnosis"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")

    def __str__(self):
        return self.user.email

