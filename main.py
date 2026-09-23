"""Консольная точка входа для каталога настольных игр."""

from games import find_games, sort_games
from reviews import create_review
from storage import load_catalog, save_catalog
from users import find_user


def show_games(games, reviews) -> None:
    """Вывести карточки всех игр."""
    if not games:
        print("В каталоге пока нет игр.")
        return
    for game in sort_games(games):
        print(game.card(reviews))


def show_search(games, reviews) -> None:
    """Запросить строку и показать подходящие игры."""
    query = input("Название для поиска: ").strip()
    show_games(find_games(games, query), reviews)


def add_rating(games, users, ratings) -> None:
    """Добавить оценку, проверив введённые идентификаторы и число."""
    try:
        game_id = int(input("ID игры: "))
        user_id = int(input("ID пользователя: "))
        score = int(input("Оценка от 0 до 10: "))
        comment = input("Короткий отзыв: ").strip()
        game = next((item for item in games if item.id == game_id), None)
        user = find_user(users, user_id)
        if game is None:
            raise ValueError("Игра с таким ID не найдена.")
        if user is None:
            raise ValueError("Пользователь с таким ID не найден.")
        rating = create_review(ratings, game, user, score, comment)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return
    ratings.append(rating)
    print("Оценка добавлена.")


def main() -> None:
    """Запустить простое меню приложения."""
    categories, games, users, ratings = load_catalog()
    while True:
        print("\nКаталог настольных игр")
        print("1 - показать игры")
        print("2 - найти игру")
        print("3 - добавить оценку")
        print("0 - сохранить и выйти")
        command = input("Выберите действие: ").strip()
        if command == "1":
            show_games(games, ratings)
        elif command == "2":
            show_search(games, ratings)
        elif command == "3":
            add_rating(games, users, ratings)
        elif command == "0":
            save_catalog(categories, games, users, ratings)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
