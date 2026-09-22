"""Консольная точка входа для каталога настольных игр."""

from categories import find_category
from games import find_games, sort_games
from ratings import create_rating
from storage import load_catalog, save_catalog


def show_games(games, categories, ratings) -> None:
    """Вывести карточки всех игр."""
    if not games:
        print("В каталоге пока нет игр.")
        return
    for game in sort_games(games):
        category = find_category(categories, game.category_id)
        category_name = category.name if category else "Без категории"
        print(game.card(category_name, ratings))


def show_search(games, categories, ratings) -> None:
    """Запросить строку и показать подходящие игры."""
    query = input("Название для поиска: ").strip()
    show_games(find_games(games, query), categories, ratings)


def add_rating(games, users, ratings) -> None:
    """Добавить оценку, проверив введённые идентификаторы и число."""
    try:
        game_id = int(input("ID игры: "))
        user_id = int(input("ID пользователя: "))
        score = int(input("Оценка от 0 до 10: "))
        comment = input("Короткий отзыв: ").strip()
        rating = create_rating(ratings, games, users, game_id, user_id, score, comment)
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
            show_games(games, categories, ratings)
        elif command == "2":
            show_search(games, categories, ratings)
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
