from django.core.management.base import BaseCommand

from apps.imports.sheets import TeamImportService


class Command(BaseCommand):
    help = ""

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        service = TeamImportService()
        service.store()

        self.stdout.write(self.style.SUCCESS("Team data successfully retrieved"))
