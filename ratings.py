"""Операции с оценками и проверки правил предметной области."""

from models import Game, Rating, User


def create_rating(
    ratings: list[Rating],
    games: list[Game],
    users: list[User],
    game_id: int,
    user_id: int,
    score: int,
    comment: str,
) -> Rating:
    """Создать оценку, проверив существование объектов и диапазон числа."""
    if not any(game.id == game_id for game in games):
        raise ValueError("Игра с таким ID не найдена.")
    if not any(user.id == user_id for user in users):
        raise ValueError("Пользователь с таким ID не найден.")
    if not 0 <= score <= 10:
        raise ValueError("Оценка должна быть целым числом от 0 до 10.")
    new_id = max((rating.id for rating in ratings), default=0) + 1
    return Rating(new_id, game_id, user_id, score, comment.strip())


def ratings_for_game(ratings: list[Rating], game_id: int) -> list[Rating]:
    """Вернуть все оценки конкретной игры."""
    return [rating for rating in ratings if rating.game_id == game_id]
