from django.core.management.base import BaseCommand

from portal.models import User


class Command(BaseCommand):
    help = """List the users.
    Usage: ``python manage.py user_list --help``"""

    def handle(self, *args, **options):
        users = User.objects.all().order_by("username")

        for user in users:
            print(f"{user.username} {user.email} {user.is_staff} {user.is_regulator}")
