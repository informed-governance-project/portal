from django.core.management.base import BaseCommand

from portal.models import ExternalToken, Module, User


class Command(BaseCommand):
    help = """Create a new access for a user to the specified service.
    Usage: ``python manage.py access_create --help``"""

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--module_name", type=str)
        parser.add_argument("--token", type=str)

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist:
            return "Unknown user."

        try:
            module = Module.objects.get(name=options["module_name"])
        except User.DoesNotExist:
            return "Unknown user."

        ExternalToken.objects.create(
            token=options["token"],
            module=module,
            user=user,
        )

        return "New access created."
