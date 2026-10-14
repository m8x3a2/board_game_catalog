"""Тесты страниц раздела отзывов."""

from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse


class RatingsTests(SimpleTestCase):
    """Проверка страниц /reviews/ и /reviews/<id>/."""

    def test_named_urls(self):
        """Именованные маршруты пространства имён ratings строят адреса."""
        self.assertEqual(reverse("ratings:list"), "/reviews/")
        self.assertEqual(reverse("ratings:detail", args=[1]), "/reviews/1/")

    def test_reviews_list(self):
        """Список отзывов строится по данным data/ratings.json."""
        response = self.client.get(reverse("ratings:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ratings/review_list.html")
        self.assertTemplateUsed(response, "ratings/includes/review_item.html")
        self.assertContains(response, 'href="/reviews/1/"')
        self.assertContains(response, "Мария")

    def test_empty_reviews_list(self):
        """При отсутствии отзывов выводится сообщение из {% empty %}."""
        with patch("ratings.views.load_catalog", return_value=([], [], [], [])):
            response = self.client.get(reverse("ratings:list"))
        self.assertContains(response, "Отзывов пока нет.")

    def test_review_detail(self):
        """Отзыв показывает связанные объекты игры и пользователя."""
        response = self.client.get(reverse("ratings:detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "ratings/review_detail.html")
        self.assertContains(response, "Каркассон")
        self.assertContains(response, 'href="/games/1/"')
        self.assertContains(response, "9/10")

    def test_missing_review_returns_404(self):
        """Несуществующий отзыв возвращает код 404."""
        response = self.client.get("/reviews/999/")
        self.assertContains(response, "Отзыв не найден", status_code=404)
