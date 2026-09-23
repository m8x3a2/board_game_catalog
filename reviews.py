"""Операции с отзывами, связывающими игры и пользователей."""

from models import Game, Review, User


def create_review(
    reviews: list[Review],
    game: Game,
    user: User,
    score: int,
    comment: str,
) -> Review:
    """Создать отзыв, передавая в него экземпляры Game и User."""
    if not 0 <= score <= 10:
        raise ValueError("Оценка должна быть целым числом от 0 до 10.")
    new_id = max((review.id for review in reviews), default=0) + 1
    return Review(new_id, game, user, score, comment.strip())


def reviews_for_game(reviews: list[Review], game: Game) -> list[Review]:
    """Вернуть отзывы, связанные с переданным объектом игры."""
    return [review for review in reviews if review.game is game]
