"""View-функции главной страницы и собственной страницы ошибки 404."""

from django.shortcuts import render

from storage import load_catalog


def index(request):
    """Главная страница: описание каталога и переходы к разделам."""
    categories, games, users, reviews = load_catalog()
    context = {
        "categories": categories,
        "games": games,
        "users": users,
        "reviews": reviews,
    }
    return render(request, "homepage/index.html", context)


def page_not_found(request, exception):
    """Собственная страница ошибки 404 для любого неизвестного адреса."""
    return render(request, "homepage/404.html", status=404)
