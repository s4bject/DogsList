"""Конфигурация приложения для модели собак."""

from django.apps import AppConfig


class DogsConfig(AppConfig):
    """Конфигурация приложения 'dogs'."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dogs'
