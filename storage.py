"""Загрузка и сохранение объектов каталога в JSON-файлы."""

import json
from pathlib import Path

from models import Category, Game, Rating, User

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


def load_catalog() -> tuple[list[Category], list[Game], list[User], list[Rating]]:
    """Загрузить JSON-данные и создать объекты предметной области."""
    categories = [Category(**item) for item in _load_items("categories.json")]
    games = [Game(**item) for item in _load_items("games.json")]
    users = [User(**item) for item in _load_items("users.json")]
    ratings = [Rating(**item) for item in _load_items("ratings.json")]
    return categories, games, users, ratings


def save_catalog(
    categories: list[Category],
    games: list[Game],
    users: list[User],
    ratings: list[Rating],
) -> None:
    """Преобразовать объекты в словари и записать их в JSON."""
    _save_items("categories.json", [item.__dict__ for item in categories])
    _save_items("games.json", [item.__dict__ for item in games])
    _save_items("users.json", [item.__dict__ for item in users])
    _save_items("ratings.json", [item.__dict__ for item in ratings])
