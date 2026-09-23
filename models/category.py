"""Класс категории настольных игр."""

from dataclasses import dataclass


@dataclass
class Category:
    """Категория или жанр настольной игры."""

    id: int
    name: str
    description: str

    def __str__(self) -> str:
        """Вернуть название категории."""
        return self.name
