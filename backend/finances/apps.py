import sys

from django.apps import AppConfig


class FinancesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "finances"
    verbose_name = "Финансы"

    def ready(self):
        if "test" not in sys.argv:
            import finances.signals
