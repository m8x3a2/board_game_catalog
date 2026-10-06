"""Конфигурация приложения catalog."""

from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Настройки приложения каталога игр."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"
    verbose_name = "Каталог игр"
