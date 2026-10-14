"""Тесты страниц раздела игр."""

from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse


class CatalogTests(SimpleTestCase):
    """Проверка страниц /games/ и /games/<id>/."""

    def test_named_urls(self):
        """Именованные маршруты пространства имён catalog строят адреса."""
        self.assertEqual(reverse("catalog:list"), "/games/")
        self.assertEqual(reverse("catalog:detail", args=[1]), "/games/1/")

    def test_games_list(self):
        """Список игр строится по данным data/games.json через шаблон."""
        response = self.client.get(reverse("catalog:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/game_list.html")
        self.assertTemplateUsed(response, "catalog/includes/game_card.html")
        self.assertContains(response, "Каркассон")
        self.assertContains(response, 'href="/games/1/"')
        self.assertContains(response, "Всего игр: 2")

    def test_empty_games_list(self):
        """При пустом каталоге выводится сообщение из {% empty %}."""
        with patch("catalog.views.load_catalog", return_value=([], [], [], [])):
            response = self.client.get(reverse("catalog:list"))
        self.assertContains(response, "В каталоге пока нет игр.")

    def test_game_detail(self):
        """Карточка игры показывает категорию, рейтинг и отзывы."""
        response = self.client.get(reverse("catalog:detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/game_detail.html")
        self.assertContains(response, "Стратегия")
        self.assertContains(response, "8,5/10")
        self.assertContains(response, "Отличная механика")

    def test_missing_game_returns_404(self):
        """Несуществующая игра возвращает код 404 и сообщение шаблона."""
        response = self.client.get("/games/999/")
        self.assertContains(response, "Игра не найдена", status_code=404)
        self.assertTemplateUsed(response, "catalog/game_detail.html")
