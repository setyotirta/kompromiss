# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GoalLadder
def undo_last_action(history):
    """Откат последнего действия из истории."""
    if not history:
        print("История пуста, отменить нечего.")
        return False
    last = history.pop()
    print(f"Отменено действие: {last}")
    return True

# Пример использования с историей действий
history = [
    "Добавлена цель: Выучить Python",
    "Добавлен шаг: Начать с синтаксиса",
    "Установлен дедлайн: 2024-12-31",
    "Отменено действие: Установлен дедлайн: 2024-12-31"
]

print("История до отмены:")
for action in history:
    print(f"- {action}")

undo_last_action(history)

print("\nИстория после отмены:")
for action in history:
    print(f"- {action}")
