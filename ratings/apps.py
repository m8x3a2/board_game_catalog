"""Конфигурация приложения ratings."""

from django.apps import AppConfig


class RatingsConfig(AppConfig):
    """Настройки приложения отзывов и оценок."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "ratings"
    verbose_name = "Отзывы и оценки"
