"""View-функции раздела игр: список игр и карточка отдельной игры."""

from django.shortcuts import render

from games import find_game_by_id, sort_games
from reviews import reviews_for_game
from storage import load_catalog


def games(request):
    """Страница /games/: список игр из data/games.json."""
    _, games_list, _, reviews = load_catalog()
    game_rows = [
        {"game": game, "average": game.average_rating(reviews)}
        for game in sort_games(games_list)
    ]
    context = {
        "game_rows": game_rows,
    }
    return render(request, "catalog/game_list.html", context)


def game_detail(request, game_id):
    """Страница /games/<id>/: карточка игры с отзывами или код 404."""
    _, games_list, _, reviews = load_catalog()
    game = find_game_by_id(games_list, game_id)
    context = {
        "game": game,
    }
    if game is not None:
        context["average"] = game.average_rating(reviews)
        context["rating_label"] = game.rating_label(reviews)
        context["game_reviews"] = reviews_for_game(reviews, game)
    return render(
        request,
        "catalog/game_detail.html",
        context,
        status=404 if game is None else 200,
    )
