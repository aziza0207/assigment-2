import datetime
import factory
from factory import fuzzy
from faker import Faker
from django.utils.timezone import now
from users.models import CustomUser, Patient
from users.constants import Role

fake = Faker()


class CustomUserFactory(factory.django.DjangoModelFactory):

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    role = fuzzy.FuzzyChoice(choices=Role.values)

    class Meta:
        model = CustomUser


class PatientFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(CustomUserFactory)
    date_of_birth = now().date() - datetime.timedelta(days=3000)
    diagnoses = factory.LazyFunction(lambda: [[fake.word() for _ in range(3)]])
    created_at = now() - datetime.timedelta(days=3)

    class Meta:
        model = Patient
