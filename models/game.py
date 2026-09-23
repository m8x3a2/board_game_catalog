"""Класс настольной игры."""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Iterable

from .category import Category

if TYPE_CHECKING:
    from .review import Review


@dataclass
class Game:
    """Настольная игра, связанная с объектом категории."""

    id: int
    title: str
    category: Category
    release_year: int

    def average_rating(self, reviews: Iterable["Review"]) -> float:
        """Рассчитать среднюю оценку по отзывам этой игры."""
        scores = [review.score for review in reviews if review.game is self]
        return round(sum(scores) / len(scores), 1) if scores else 0.0

    def rating_label(self, reviews: Iterable["Review"]) -> str:
        """Вернуть текстовую метку для среднего рейтинга."""
        average = self.average_rating(reviews)
        if average >= 9:
            return "Отлично"
        if average >= 7:
            return "Хорошо"
        if average >= 5:
            return "Средне"
        return "Пока нет оценок" if average == 0 else "Плохо"

    def card(self, reviews: Iterable["Review"]) -> str:
        """Сформировать текстовую карточку игры для консоли."""
        average = self.average_rating(reviews)
        return (
            f"[{self.id}] {self.title} ({self.release_year})\n"
            f"Категория: {self.category.name}\n"
            f"Рейтинг: {average}/10 ({self.rating_label(reviews)})"
        )

    def __str__(self) -> str:
        """Вернуть название и год выпуска игры."""
        return f"{self.title} ({self.release_year})"
