"""Тесты функций поиска, сортировки, оценок и хранения JSON."""

import json

import pytest

import storage
from games import find_games, sort_games
from models import Category, Game, Rating, User
from ratings import create_rating


def test_find_and_sort_games() -> None:
    """Поиск не зависит от регистра, а сортировка не меняет исходный список."""
    games = [Game(1, "Каркассон", 1, 2000), Game(2, "Азул", 2, 2017)]

    assert find_games(games, "КАР") == [games[0]]
    assert sort_games(games) == [games[1], games[0]]


def test_create_rating_validates_score_and_links() -> None:
    """Оценка создаётся только в диапазоне 0-10 для существующих объектов."""
    games = [Game(1, "Каркассон", 1, 2000)]
    users = [User(1, "Мария")]
    ratings = []

    rating = create_rating(ratings, games, users, 1, 1, 7, "Нравится")

    assert rating.score == 7
    with pytest.raises(ValueError):
        create_rating(ratings, games, users, 1, 1, 11, "Ошибка")


def test_storage_loads_objects(monkeypatch, tmp_path) -> None:
    """Загрузка JSON создаёт объекты классов, а сохранение записывает JSON."""
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
    for filename, content in source.items():
        (tmp_path / filename).write_text(json.dumps(content), encoding="utf-8")
    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)

    categories, games, users, ratings = storage.load_catalog()
    storage.save_catalog(categories, games, users, ratings)

    assert isinstance(categories[0], Category)
    assert isinstance(games[0], Game)
    assert isinstance(users[0], User)
    assert isinstance(ratings[0], Rating)
    saved = json.loads((tmp_path / "ratings.json").read_text(encoding="utf-8"))
    assert saved[0]["score"] == 10
