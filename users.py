"""Операции с пользователями каталога."""

from models import User


def find_user(users: list[User], user_id: int) -> User | None:
    """Найти пользователя по идентификатору."""
    return next((item for item in users if item.id == user_id), None)


def add_user(users: list[User], name: str) -> User:
    """Создать пользователя с очередным идентификатором."""
    if not name.strip():
        raise ValueError("Имя пользователя не должно быть пустым.")
    new_id = max((item.id for item in users), default=0) + 1
    return User(new_id, name.strip())
