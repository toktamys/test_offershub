from django.core.management import BaseCommand

from asana_api.models import User
from asana_api.utils import AsanaApiHelper


class Command(BaseCommand):

    def handle(self, *args, **options):
        asana = AsanaApiHelper()
        User.objects.bulk_create([
            User(
                name=asana.me['name'],
                email=asana.me['email'],
                asana_id=asana.me['gid']
            )
        ])
        self.stdout.write("It's done")
