"""Тесты классов предметной области."""

from models import Category, Game, Rating, User


def test_game_calculates_average_and_label() -> None:
    """Игра рассчитывает среднюю оценку и метку качества."""
    game = Game(1, "Каркассон", 1, 2000)
    ratings = [Rating(1, 1, 1, 8, "Хорошо"), Rating(2, 1, 2, 10, "Отлично")]

    assert game.average_rating(ratings) == 9.0
    assert game.rating_label(ratings) == "Отлично"


def test_string_representations() -> None:
    """Все основные сущности имеют понятное строковое представление."""
    assert str(Category(1, "Стратегия", "Описание")) == "Стратегия"
    assert str(User(1, "Мария")) == "Мария"
    assert str(Rating(1, 1, 1, 8, "Хорошо")) == "8/10: Хорошо"
    assert str(Game(1, "Каркассон", 1, 2000)) == "Каркассон (2000)"
