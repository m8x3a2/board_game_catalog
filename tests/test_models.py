"""Тесты классов предметной области."""

from models import Category, Game, Review, User


def test_game_calculates_average_and_label() -> None:
    """Игра рассчитывает среднюю оценку и метку качества."""
    category = Category(1, "Стратегия", "Описание")
    game = Game(1, "Каркассон", category, 2000)
    user = User(1, "Мария")
    reviews = [
        Review(1, game, user, 8, "Хорошо"),
        Review(2, game, user, 10, "Отлично"),
    ]

    assert game.average_rating(reviews) == 9.0
    assert game.rating_label(reviews) == "Отлично"


def test_string_representations() -> None:
    """Все основные сущности имеют понятное строковое представление."""
    assert str(Category(1, "Стратегия", "Описание")) == "Стратегия"
    assert str(User(1, "Мария")) == "Мария"
    category = Category(1, "Стратегия", "Описание")
    game = Game(1, "Каркассон", category, 2000)
    user = User(1, "Мария")

    assert str(Review(1, game, user, 8, "Хорошо")) == "Мария: 8/10 - Хорошо"
    assert str(game) == "Каркассон (2000)"
