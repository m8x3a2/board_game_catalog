"""Тесты страниц раздела игр."""

from django.test import SimpleTestCase


class CatalogTests(SimpleTestCase):
    """Проверка страниц /games/ и /games/<id>/."""

    def test_games_list(self):
        """Список игр строится по данным data/games.json."""
        response = self.client.get("/games/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Каркассон")
        self.assertContains(response, 'href="/games/1/"')

    def test_game_detail(self):
        """Карточка игры показывает категорию, рейтинг и отзывы."""
        response = self.client.get("/games/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Стратегия")
        self.assertContains(response, "8.5/10")
        self.assertContains(response, "Отличная механика")

    def test_missing_game_returns_404(self):
        """Несуществующая игра возвращает код 404."""
        response = self.client.get("/games/999/")
        self.assertContains(response, "Игра не найдена", status_code=404)
