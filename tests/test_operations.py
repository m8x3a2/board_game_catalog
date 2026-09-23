"""Тесты функций поиска, сортировки, оценок и хранения JSON."""

import pytest

import storage
from games import find_games, sort_games
from models import Category, Game, Review, User
from reviews import create_review


def test_find_and_sort_games() -> None:
    """Поиск не зависит от регистра, а сортировка не меняет исходный список."""
    category = Category(1, "Стратегия", "Описание")
    games = [Game(1, "Каркассон", category, 2000), Game(2, "Азул", category, 2017)]

    assert find_games(games, "КАР") == [games[0]]
    assert sort_games(games) == [games[1], games[0]]


def test_create_rating_validates_score_and_links() -> None:
    """Оценка создаётся только в диапазоне 0-10 для существующих объектов."""
    category = Category(1, "Стратегия", "Описание")
    games = [Game(1, "Каркассон", category, 2000)]
    users = [User(1, "Мария")]
    ratings = []

    review = create_review(ratings, games[0], users[0], 7, "Нравится")

    assert review.game is games[0]
    assert review.user is users[0]
    assert review.score == 7
    with pytest.raises(ValueError):
        create_review(ratings, games[0], users[0], 11, "Ошибка")


def test_storage_loads_and_saves_objects(monkeypatch) -> None:
    """JSON-словарь преобразуется в объекты и обратно без временных файлов."""
    source = {
        "categories.json": [
            {"id": 1, "name": "Семейная", "description": "Для всех"},
        ],
        "games.json": [
            {
                "id": 1,
                "title": "Азул",
                "category_id": 1,
                "release_year": 2017,
            },
        ],
        "users.json": [{"id": 1, "name": "Ирина"}],
        "ratings.json": [
            {
                "id": 1,
                "game_id": 1,
                "user_id": 1,
                "score": 10,
                "comment": "Супер",
            },
        ],
    }

    def load_items(filename: str) -> list[dict]:
        return source[filename]

    saved_items: dict[str, list[dict]] = {}

    def save_items(filename: str, items: list[dict]) -> None:
        saved_items[filename] = items

    monkeypatch.setattr(storage, "_load_items", load_items)
    monkeypatch.setattr(storage, "_save_items", save_items)

    categories, games, users, ratings = storage.load_catalog()
    storage.save_catalog(categories, games, users, ratings)

    assert isinstance(categories[0], Category)
    assert isinstance(games[0], Game)
    assert isinstance(users[0], User)
    assert isinstance(ratings[0], Review)
    assert ratings[0].game is games[0]
    assert ratings[0].user is users[0]
    assert saved_items["ratings.json"][0]["game_id"] == 1
