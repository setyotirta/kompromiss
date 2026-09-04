# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: GoalLadder
def demo():
    from datetime import datetime, timedelta

    # Создаём цели для демонстрации
    goals = [
        {
            "id": 1,
            "title": "Изучить Python",
            "description": "Пройти курс по основам Python",
            "deadline": datetime.now() + timedelta(days=7),
            "steps": [
                {"title": "Установка окружения", "done": True},
                {"title": "Переменные и типы", "done": True},
                {"title": "Условия и циклы", "done": True},
                {"title": "Функции", "done": True},
                {"title": "ООП", "done": False},
            ],
            "created": datetime.now() - timedelta(days=2),
        },
        {
            "id": 2,
            "title": "Написать Todo-приложение",
            "description": "Создать CLI-приложение для управления задачами",
            "deadline": datetime.now() + timedelta(days=14),
            "steps": [
                {"title": "Проектировать структуру", "done": True},
                {"title": "Реализовать CRUD", "done": True},
                {"title": "Добавить фильтрацию", "done": False},
                {"title": "Написать тесты", "done": False},
            ],
            "created": datetime.now() - timedelta(days=5),
        },
        {
            "id": 3,
            "title": "Почитать книги",
            "description": "Прочитать 3 книги из списка",
            "deadline": datetime.now() + timedelta(days=30),
            "steps": [
                {"title": "Выбрать книги", "done": True},
                {"title": "Прочитать первую", "done": True},
                {"title": "Прочитать вторую", "done": False},
                {"title": "Прочитать третью", "done": False},
            ],
            "created": datetime.now() - timedelta(days=1),
        },
    ]

    print("=" * 50)
    print("🚀 Демо: Трекер целей GoalLadder")
    print("=" * 50)

    for goal in goals:
        progress = goal["done_steps"] / len(goal["steps"])
        print(f"\n🎯 {goal['title']}")
        print(f"   Прогресс: {progress:.0%}")
        print(f"   Дедлайн: {goal['deadline'].strftime('%d.%m.%Y')}")
        print(f"   Создана: {goal['created'].strftime('%d.%m.%Y')}")
        print(f"   Шаги: {sum(1 for s in goal['steps'] if s['done'])}/{len(goal['steps'])}")

    print("\n" + "=" * 50)
    print("✅ Демо завершена")
    print("=" * 50)
