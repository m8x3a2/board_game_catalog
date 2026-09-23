"""Операции с коллекцией объектов Game."""

from models import Category, Game


def find_games(games: list[Game], query: str) -> list[Game]:
    """Найти игры, название которых содержит заданную строку."""
    normalized_query = query.strip().lower()
    return [game for game in games if normalized_query in game.title.lower()]


def filter_games_by_category(
    games: list[Game],
    category: Category,
) -> list[Game]:
    """Отобрать игры по объекту категории."""
    return [game for game in games if game.category is category]


def sort_games(games: list[Game]) -> list[Game]:
    """Вернуть новый список игр, отсортированный по названию."""
    return sorted(games, key=lambda game: game.title.lower())


def add_game(
    games: list[Game],
    title: str,
    category: Category,
    release_year: int,
) -> Game:
    """Создать игру с очередным идентификатором."""
    if not title.strip():
        raise ValueError("Название игры не должно быть пустым.")
    if release_year < 1900:
        raise ValueError("Год выпуска должен быть не меньше 1900.")
    new_id = max((game.id for game in games), default=0) + 1
    return Game(new_id, title.strip(), category, release_year)
