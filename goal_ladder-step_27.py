# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: GoalLadder
def reset_demo_data():
    """Сбросить демо-данные: очистить цели, шаги, достижения."""
    goals = []
    steps = {}
    achievements = []
    stats = {"total_goals": 0, "completed_goals": 0, "current_step": None}
    return goals, steps, achievements, stats

def clear_state():
    """Очистить все данные приложения."""
    print("Состояние очищено. Приложение готово к работе.")
