# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GoalLadder
def print_project_metrics(goals):
    """Показывает ключевые метрики проекта: прогресс, дедлайны, достижения."""
    total = len(goals)
    if not total:
        print("Нет целей в проекте.")
        return
    active = sum(1 for g in goals if g["status"] == "active")
    completed = sum(1 for g in goals if g["status"] == "completed")
    overdue = sum(1 for g in goals if g.get("deadline", None) and g.get("created_at", "") <= g["deadline"])
    print(f"Всего целей: {total}")
    print(f"Активные: {active}, Завершённые: {completed}")
    print(f"Запланировано к дедлайнам: {overdue}")
