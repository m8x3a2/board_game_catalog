"""Операции с категориями игр."""

from models import Category


def find_category(categories: list[Category], category_id: int) -> Category | None:
    """Найти категорию по идентификатору."""
    return next((item for item in categories if item.id == category_id), None)


def add_category(categories: list[Category], name: str, description: str) -> Category:
    """Создать и вернуть новую категорию."""
    if not name.strip():
        raise ValueError("Название категории не должно быть пустым.")
    new_id = max((item.id for item in categories), default=0) + 1
    return Category(new_id, name.strip(), description.strip())
