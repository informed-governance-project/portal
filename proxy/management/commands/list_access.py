from django.core.management.base import BaseCommand

from proxy.models import ExternalToken


class Command(BaseCommand):
    help = """List the different accesses.
    Usage: ``python manage.py revoke_access --help``"""

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--module_name", type=str)

    def handle(self, *args, **options):

        accesses = ExternalToken.objects.all().order_by("user__username")

        print("Username" + " " * 15 + "Module name")
        print("-" * 34)
        for access in accesses:
            print("{} {} {}".format(access.user.username, " " * 15, access.module_name))
