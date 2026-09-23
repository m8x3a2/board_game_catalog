"""Класс отзыва, связывающего игру и пользователя."""

from dataclasses import dataclass

from .game import Game
from .user import User


@dataclass
class Review:
    """Отзыв пользователя об игре с оценкой от 0 до 10."""

    id: int
    game: Game
    user: User
    score: int
    comment: str

    def __str__(self) -> str:
        """Вернуть отзыв вместе с именами связанных объектов."""
        return f"{self.user.name}: {self.score}/10 - {self.comment}"
