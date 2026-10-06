"""Тесты главной страницы и обработчика ошибки 404."""

from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    """Проверка цикла URL → view → response для приложения homepage."""

    def test_index_page(self):
        """Главная страница открывается и содержит навигацию."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Каталог настольных игр")
        self.assertContains(response, 'href="/games/"')
        self.assertContains(response, 'href="/reviews/"')
        self.assertContains(response, "bootstrap.min.css")

    def test_unknown_url_uses_custom_404(self):
        """Неизвестный адрес обрабатывается собственной страницей 404."""
        response = self.client.get("/nonexistent/")
        self.assertContains(response, "страница не найдена", status_code=404)
