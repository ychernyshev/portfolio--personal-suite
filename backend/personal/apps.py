# SPDX-License-Identifier: AGPL-3.0-or-later
from django.apps import AppConfig


class PersonalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal'

    def ready(self):
        import personal.services.signals