"""Класс пользователя каталога."""

from dataclasses import dataclass


@dataclass
class User:
    """Пользователь, который может оставлять отзывы."""

    id: int
    name: str

    def __str__(self) -> str:
        """Вернуть имя пользователя."""
        return self.name
