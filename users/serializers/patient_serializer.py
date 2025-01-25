from rest_framework import serializers
from users.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.CharField(source="user.email")

    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "email", "diagnoses")
