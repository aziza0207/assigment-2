import os
from dotenv import load_dotenv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


load_dotenv()


DEFAULT_ADMIN_EMAIL = os.environ.get("DEFAULT_ADMIN_EMAIL")
DEFAULT_ADMIN_PASSWORD = os.environ.get("DEFAULT_ADMIN_PASSWORD")


class Command(BaseCommand):
    help = "Creates a default admin user if not already present."

    def handle(self, *args, **options):
        User = get_user_model()

        if not User.objects.filter(email=DEFAULT_ADMIN_EMAIL).exists():
            User.objects.create_superuser(
                email=DEFAULT_ADMIN_EMAIL,
                password=DEFAULT_ADMIN_PASSWORD,

            )
            self.stdout.write(self.style.SUCCESS(f"Admin user '{DEFAULT_ADMIN_EMAIL}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Admin user '{DEFAULT_ADMIN_EMAIL}' already exists."))
