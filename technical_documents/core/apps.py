# Author: Ameera Abdullah, Juri Khushayl
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        post_migrate.connect(load_fixture, sender=self)


def load_fixture(sender, **kwargs):
    call_command('loaddata', 'core/fixtures/minigames_locations.json')
