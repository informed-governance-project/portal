from django.core.management.base import BaseCommand

from portal.models import Module


class Command(BaseCommand):
    help = """Create a new module/apllication.
    Usage: ``python manage.py amodule_create --help``"""

    def add_arguments(self, parser):
        parser.add_argument("--name", type=str)
        parser.add_argument("--path", type=str)
        parser.add_argument("--upstream", type=str)

    def handle(self, *args, **options):
        Module.objects.create(
            name=options["name"],
            path=options["path"],
            upstream=options["upstream"],
        )

        return "New module created."
