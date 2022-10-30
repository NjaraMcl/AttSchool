from django.apps import AppConfig


class AppmainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "appMain"

    def ready(self):
        import appMain.signals
