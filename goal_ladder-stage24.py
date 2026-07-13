# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GoalLadder
def show_goal_record(goal):
    """Компактный вывод одной записи цели с ключевыми деталями."""
    status = "✅ Выполнено" if goal["completed"] else (
        "⏳ В процессе" if goal.get("deadline") and goal["deadline"] > datetime.now() else
        "❌ Пропущен" if goal.get("deadline") else "📋 Без дедлайна"
    )
    print(f"\n{'='*50}")
    print(f"  🎯 Запись: #{goal['id']} — {goal['title']}")
    print(f"  Статус:   {status}")
    if goal.get("steps"):
        total = len(goal["steps"])
        done = sum(1 for s in goal["steps"] if s.get("done"))
        pct = round(done / total * 100) if total else 0
        bar = "█" * int(pct/5) + "░" * (20 - int(pct/5))
        print(f"  Прогресс: [{bar}] {pct}% ({done}/{total})")
    if goal.get("deadline"):
        days_left = (goal["deadline"] - datetime.now()).days
        print(f"  Дедлайн:  {goal['deadline'].strftime('%d.%m')} ({days_left} дн.)")
    if goal.get("note"):
        print(f"  Примечание: {goal['note']}")
