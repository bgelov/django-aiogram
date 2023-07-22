from django.apps import AppConfig


class BanbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'banbot'

    def ready(self):
        from banbot.handlers import users, groups