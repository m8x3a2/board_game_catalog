"""View-функции раздела игр: список игр и карточка отдельной игры."""

from django.http import HttpResponse
from django.utils.html import escape

from games import find_game_by_id, sort_games
from homepage.views import page, score_badge
from reviews import reviews_for_game
from storage import load_catalog


def games(request):
    """Страница /games/: список игр из data/games.json."""
    _, games_list, _, reviews = load_catalog()
    items = ""
    for game in sort_games(games_list):
        average = game.average_rating(reviews)
        items += f"""
        <li class="list-group-item d-flex justify-content-between
                   align-items-center">
            <div>
                <a href="/games/{game.id}/">{escape(game.title)}</a>
                <small class="text-muted">
                    {game.release_year} · {escape(game.category.name)}
                </small>
            </div>
            <span class="badge {score_badge(average)}">{average}/10</span>
        </li>
        """
    if not items:
        items = '<li class="list-group-item">В каталоге пока нет игр.</li>'
    content = f"""
    <h1>Игры</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Каталог – игры", content))


def game_detail(request, game_id):
    """Страница /games/<id>/: карточка игры с отзывами или код 404."""
    _, games_list, _, reviews = load_catalog()
    game = find_game_by_id(games_list, game_id)
    if game is None:
        content = """
        <h1 class="text-danger">Игра не найдена</h1>
        <a href="/games/" class="btn btn-outline-secondary">
            ← к списку игр
        </a>
        """
        return HttpResponse(
            page("Игра не найдена", content),
            status=404,
        )

    average = game.average_rating(reviews)
    review_items = ""
    for review in reviews_for_game(reviews, game):
        review_items += f"""
        <li class="list-group-item">
            <span class="badge {score_badge(review.score)}">
                {review.score}/10
            </span>
            <a href="/reviews/{review.id}/">{escape(review.user.name)}</a>:
            {escape(review.comment)}
        </li>
        """
    if not review_items:
        review_items = '<li class="list-group-item">Отзывов пока нет.</li>'

    content = f"""
    <div class="card mb-4">
        <div class="card-body">
            <h5 class="card-title">{escape(game.title)}</h5>
            <p class="card-text"><strong>ID:</strong> {game.id}</p>
            <p class="card-text">
                <strong>Год выпуска:</strong> {game.release_year}
            </p>
            <p class="card-text">
                <strong>Категория:</strong> {escape(game.category.name)}
                <br>
                <small class="text-muted">
                    {escape(game.category.description)}
                </small>
            </p>
            <p class="card-text">
                <strong>Средняя оценка:</strong>
                <span class="badge {score_badge(average)}">{average}/10</span>
                {game.rating_label(reviews)}
            </p>
            <a href="/games/" class="btn btn-outline-secondary">
                ← к списку игр
            </a>
        </div>
    </div>
    <h2 class="h4">Отзывы</h2>
    <ul class="list-group">{review_items}</ul>
    """
    return HttpResponse(
        page(escape(game.title), content),
        status=200,
    )
