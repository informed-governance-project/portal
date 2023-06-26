from django.core.management.base import BaseCommand

from proxy.models import ExternalToken, User


class Command(BaseCommand):
    help = """Revoke an access to a user for a specified service.
    Usage: ``python manage.py revoke_access --help``"""

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--module_name", type=str)

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist:
            return "Unknown user."
        try:
            token = ExternalToken.objects.get(
                user=user, module_path=options["module_name"]
            )
            token.delete()
        except ExternalToken.DoesNotExist:
            return "Unknown module."
        except Exception:
            return "Error."

        return "Access revoked."
