"""View-функции главной страницы и общий HTML-каркас всех страниц."""

from django.http import HttpResponse

from storage import load_catalog


def page(title: str, content: str) -> str:
    """Собрать HTML-документ с Bootstrap и навигацией вокруг содержимого."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
    <style>
        body {{ background-color: #f6f4ef; }}
        main {{ padding-top: 2rem; padding-bottom: 2rem; }}
    </style>
</head>
<body>
    <nav class="navbar navbar-expand bg-dark" data-bs-theme="dark">
        <div class="container">
            <a class="navbar-brand" href="/">Каталог настольных игр</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/">Главная</a>
                <a class="nav-link" href="/games/">Игры</a>
                <a class="nav-link" href="/reviews/">Отзывы</a>
            </div>
        </div>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def score_badge(score: float) -> str:
    """Вернуть Bootstrap-класс бейджа для оценки от 0 до 10."""
    if score >= 9:
        return "bg-success"
    if score >= 7:
        return "bg-primary"
    if score >= 5:
        return "bg-warning text-dark"
    return "bg-secondary" if score == 0 else "bg-danger"


def index(request):
    """Главная страница: описание каталога и переходы к разделам."""
    categories, games, users, reviews = load_catalog()
    content = f"""
    <h1 class="display-4">Каталог настольных игр</h1>
    <p class="lead">
        Учёт настольных игр, их категорий и отзывов пользователей
        с оценкой от 0 до 10.
    </p>
    <ul class="list-inline text-muted">
        <li class="list-inline-item">Игр: {len(games)}</li>
        <li class="list-inline-item">Категорий: {len(categories)}</li>
        <li class="list-inline-item">Пользователей: {len(users)}</li>
        <li class="list-inline-item">Отзывов: {len(reviews)}</li>
    </ul>
    <p>Основные разделы:</p>
    <a href="/games/" class="btn btn-primary me-2">Игры</a>
    <a href="/reviews/" class="btn btn-secondary">Отзывы</a>
    """
    return HttpResponse(page("Каталог настольных игр", content))


def page_not_found(request, exception):
    """Собственная страница ошибки 404 для любого неизвестного адреса."""
    content = """
    <h1 class="text-danger">404 – страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 – страница не найдена", content),
        status=404,
    )
