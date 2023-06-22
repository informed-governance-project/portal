from django.core.management.base import BaseCommand

from proxy.models import ExternalToken, User


class Command(BaseCommand):
    help = """Create a new access for a user to the specified service.
    Usage: ``python manage.py create_access --help``"""

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--module_path", type=str)
        parser.add_argument("--module_name", type=str)
        parser.add_argument("--token", type=str)

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist:
            print("Unknown user.")

        ExternalToken.objects.create(
            token=options["token"],
            module_name=options["module_path"],
            module_path=options["module_name"],
            user=user,
        )

        print("New access created.")
