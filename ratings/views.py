"""View-функции раздела отзывов: список отзывов и отдельный отзыв."""

from django.http import HttpResponse
from django.utils.html import escape

from homepage.views import page, score_badge
from reviews import find_review_by_id
from storage import load_catalog


def reviews(request):
    """Страница /reviews/: список отзывов из data/ratings.json."""
    _, _, _, reviews_list = load_catalog()
    items = ""
    for review in reviews_list:
        items += f"""
        <li class="list-group-item d-flex justify-content-between
                   align-items-center">
            <a href="/reviews/{review.id}/">
                {escape(review.game.title)} – {escape(review.user.name)}
            </a>
            <span class="badge {score_badge(review.score)}">
                {review.score}/10
            </span>
        </li>
        """
    if not items:
        items = '<li class="list-group-item">Отзывов пока нет.</li>'
    content = f"""
    <h1>Отзывы</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Каталог – отзывы", content))


def review_detail(request, review_id):
    """Страница /reviews/<id>/: отзыв со связанными игрой и пользователем."""
    _, _, _, reviews_list = load_catalog()
    review = find_review_by_id(reviews_list, review_id)
    if review is None:
        content = """
        <h1 class="text-danger">Отзыв не найден</h1>
        <a href="/reviews/" class="btn btn-outline-secondary">
            ← к списку отзывов
        </a>
        """
        return HttpResponse(
            page("Отзыв не найден", content),
            status=404,
        )

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Отзыв №{review.id}</h5>
            <p class="card-text">
                Игра:
                <a href="/games/{review.game.id}/">
                    {escape(review.game.title)}
                </a>
            </p>
            <p class="card-text">
                Пользователь: {escape(review.user.name)}
            </p>
            <p class="card-text">
                Оценка:
                <span class="badge {score_badge(review.score)}">
                    {review.score}/10
                </span>
            </p>
            <p class="card-text">
                Комментарий: {escape(review.comment)}
            </p>
            <a href="/reviews/" class="btn btn-outline-secondary">
                ← к списку отзывов
            </a>
        </div>
    </div>
    """
    return HttpResponse(
        page(f"Отзыв №{review.id}", content),
        status=200,
    )
