# Author: Ameera Abdullah, Juri Khushayl
from django.apps import AppConfig

# Create an app ~ Ameera
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
     
    # Import the core.signals module to connect signal handlers. ~ Juri
    def ready(self):
        import core.signals