"""Маршруты приложения ratings (подключены с префиксом reviews/)."""

from django.urls import path

from . import views

app_name = "ratings"

urlpatterns = [
    path("", views.reviews, name="list"),
    path("<int:review_id>/", views.review_detail, name="detail"),
]
