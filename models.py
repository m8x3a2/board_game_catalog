"""Классы предметной области каталога настольных игр."""

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Category:
    """Категория или жанр настольной игры."""

    id: int
    name: str
    description: str

    def __str__(self) -> str:
        """Вернуть понятное строковое представление категории."""
        return self.name


@dataclass
class User:
    """Пользователь, который может оставлять оценки."""

    id: int
    name: str

    def __str__(self) -> str:
        """Вернуть имя пользователя."""
        return self.name


@dataclass
class Rating:
    """Оценка игры пользователем: число от 0 до 10 и комментарий."""

    id: int
    game_id: int
    user_id: int
    score: int
    comment: str

    def __str__(self) -> str:
        """Вернуть краткое представление оценки."""
        return f"{self.score}/10: {self.comment}"


@dataclass
class Game:
    """Настольная игра, принадлежащая одной категории."""

    id: int
    title: str
    category_id: int
    release_year: int

    def average_rating(self, ratings: Iterable[Rating]) -> float:
        """Рассчитать среднюю оценку игры или вернуть 0 при её отсутствии."""
        scores = [rating.score for rating in ratings if rating.game_id == self.id]
        return round(sum(scores) / len(scores), 1) if scores else 0.0

    def rating_label(self, ratings: Iterable[Rating]) -> str:
        """Вернуть текстовую метку для среднего рейтинга."""
        average = self.average_rating(ratings)
        if average >= 9:
            return "Отлично"
        if average >= 7:
            return "Хорошо"
        if average >= 5:
            return "Средне"
        return "Пока нет оценок" if average == 0 else "Плохо"

    def card(self, category_name: str, ratings: Iterable[Rating]) -> str:
        """Сформировать текстовую карточку игры для консоли."""
        average = self.average_rating(ratings)
        return (
            f"[{self.id}] {self.title} ({self.release_year})\n"
            f"Категория: {category_name}\n"
            f"Рейтинг: {average}/10 ({self.rating_label(ratings)})"
        )

    def __str__(self) -> str:
        """Вернуть название и год выпуска игры."""
        return f"{self.title} ({self.release_year})"
