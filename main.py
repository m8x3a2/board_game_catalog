from datetime import date

# Данные об игре
game_name = "Шахматы"
category = "Стратегия"
user_name = "Алексей"
rating = 8.5

# Функция 1: Статус рекомендации (как в твоем примере)
def get_recommendation(rating):
    if rating >= 8.0:
        return "Отличная игра! Рекомендуем"
    elif rating >= 7.0:
        return "Хорошая игра, можно купить"
    else:
        return "На любителя"

# Функция 2: Поиск по категории
def get_category_message(category):
    if category == "Стратегия":
        return "Игры этой категории развивают мышление"
    elif category == "Карточная":
        return "Отличный выбор для вечеринки"
    else:
        return "Интересная категория"

# Функция 3: Статус пользователя (активен или новичок)
def get_user_status(rating):
    if rating >= 7:
        return "Опытный игрок"
    else:
        return "Новичок"

# Вывод информации
print("🎲 КАТАЛОГ НАСТОЛЬНЫХ ИГР")
print(f"Игра: {game_name}")
print(f"Категория: {category}")
print(f"Пользователь: {user_name}")
print(f"Оценка: {rating} из 10")
print(f"Статус: {get_recommendation(rating)}")
print(f"Совет: {get_category_message(category)}")
print(f"Уровень пользователя: {get_user_status(rating)}")
print(f"Дата: {date.today()}")