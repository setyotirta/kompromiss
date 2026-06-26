# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GoalLadder
def generate_summary(data):
    goals = data.get("goals", [])
    achievements = [g for g in goals if g["status"] == "completed"]
    pending = [g for g in goals if g["status"] != "completed"]
    total_steps = sum(len(g.get("steps", [])) for g in goals)
    completed_steps = sum(
        len([s for s in g.get("steps", []) if s.get("done")])
        for g in achievements
    )
    deadline_overdue = [g for g in pending if g.get("deadline")] and (
        any(g["deadline"] < datetime.now() for g in pending) or False
    )
    overdue_goals = [g for g in pending if g.get("deadline") and g["deadline"] < datetime.now()]

    summary_lines = []
    summary_lines.append(f"Всего целей: {len(goals)}")
    summary_lines.append(f"Достигнуто: {len(achievements)}/{len(goals)} ({100*len(achievements)/max(len(goals), 1):.0f}%)")
    summary_lines.append(f"Выполнено шагов: {completed_steps}/{total_steps}")
    if overdue_goals:
        summary_lines.append(f"⚠️ Просрочено целей: {len(overdue_goals)}")
    else:
        summary_lines.append("✅ Все цели в графике")

    print("\n📊 СВОДКА ПО ЦЕЛЯМ:")
    for line in summary_lines:
        print(line)
