"""Маршруты приложения catalog (подключены с префиксом games/)."""

from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.games, name="list"),
    path("<int:game_id>/", views.game_detail, name="detail"),
]
