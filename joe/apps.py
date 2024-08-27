from django.apps import AppConfig


class JoeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'joe'

    def ready(self):
        import joe.signals
