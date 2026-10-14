"""Тесты главной страницы, базового шаблона и обработчика ошибки 404."""

from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    """Проверка цикла URL → view → context → template для homepage."""

    def test_index_page(self):
        """Главная страница строится из шаблона и содержит навигацию."""
        response = self.client.get(reverse("homepage:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage/index.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "includes/navigation.html")
        self.assertContains(response, "Каталог настольных игр")
        self.assertContains(response, 'href="/games/"')
        self.assertContains(response, 'href="/reviews/"')
        self.assertContains(response, "Игр: 2")

    def test_static_files_connected(self):
        """Базовый шаблон подключает Bootstrap, свои CSS, JS и логотип."""
        response = self.client.get("/")
        self.assertContains(response, "bootstrap.min.css")
        self.assertContains(response, "/static/homepage/css/style.css")
        self.assertContains(response, "/static/homepage/js/main.js")
        self.assertContains(response, "/static/homepage/img/logo.png")
        self.assertContains(response, 'id="current-year"')

    def test_unknown_url_uses_custom_404(self):
        """Неизвестный адрес обрабатывается собственной страницей 404."""
        response = self.client.get("/nonexistent/")
        self.assertContains(response, "страница не найдена", status_code=404)
