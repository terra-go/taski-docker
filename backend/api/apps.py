"""Application configuration for the API app."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for the API Django application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
