"""Загрузка и сохранение объектов каталога в JSON-файлы."""

import json
from pathlib import Path

from models import Category, Game, Review, User

DATA_DIR = Path(__file__).parent / "data"


def _load_items(filename: str) -> list[dict]:
    """Прочитать список словарей из JSON-файла."""
    with (DATA_DIR / filename).open(encoding="utf-8") as file:
        return json.load(file)


def _save_items(filename: str, items: list[dict]) -> None:
    """Сохранить список словарей в JSON-файл."""
    DATA_DIR.mkdir(exist_ok=True)
    with (DATA_DIR / filename).open("w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=2)


def load_catalog() -> tuple[list[Category], list[Game], list[User], list[Review]]:
    """Загрузить JSON и восстановить связи объектов Game, User и Review."""
    categories = [Category(**item) for item in _load_items("categories.json")]
    categories_by_id = {category.id: category for category in categories}
    games = [
        Game(
            item["id"],
            item["title"],
            categories_by_id[item["category_id"]],
            item["release_year"],
        )
        for item in _load_items("games.json")
    ]
    users = [User(**item) for item in _load_items("users.json")]
    games_by_id = {game.id: game for game in games}
    users_by_id = {user.id: user for user in users}
    reviews = [
        Review(
            item["id"],
            games_by_id[item["game_id"]],
            users_by_id[item["user_id"]],
            item["score"],
            item["comment"],
        )
        for item in _load_items("ratings.json")
    ]
    return categories, games, users, reviews


def save_catalog(
    categories: list[Category],
    games: list[Game],
    users: list[User],
    reviews: list[Review],
) -> None:
    """Преобразовать объекты в JSON, сохранив ID связанных объектов."""
    _save_items("categories.json", [item.__dict__ for item in categories])
    _save_items(
        "games.json",
        [
            {
                "id": game.id,
                "title": game.title,
                "category_id": game.category.id,
                "release_year": game.release_year,
            }
            for game in games
        ],
    )
    _save_items("users.json", [item.__dict__ for item in users])
    _save_items(
        "ratings.json",
        [
            {
                "id": review.id,
                "game_id": review.game.id,
                "user_id": review.user.id,
                "score": review.score,
                "comment": review.comment,
            }
            for review in reviews
        ],
    )
