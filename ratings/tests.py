"""Тесты страниц раздела отзывов."""

from django.test import SimpleTestCase


class RatingsTests(SimpleTestCase):
    """Проверка страниц /reviews/ и /reviews/<id>/."""

    def test_reviews_list(self):
        """Список отзывов строится по данным data/ratings.json."""
        response = self.client.get("/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/reviews/1/"')
        self.assertContains(response, "Мария")

    def test_review_detail(self):
        """Отзыв показывает связанные объекты игры и пользователя."""
        response = self.client.get("/reviews/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Каркассон")
        self.assertContains(response, 'href="/games/1/"')
        self.assertContains(response, "9/10")

    def test_missing_review_returns_404(self):
        """Несуществующий отзыв возвращает код 404."""
        response = self.client.get("/reviews/999/")
        self.assertContains(response, "Отзыв не найден", status_code=404)
