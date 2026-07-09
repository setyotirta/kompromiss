# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GoalLadder
def check_overdue_reminders():
    overdue = []
    now = datetime.now()
    for goal in goals:
        if goal.reminder and goal.reminder.date <= now:
            if not goal.completed and (goal.reminder.repeat or goal.reminder.date):
                overdue.append(goal)
    if overdue:
        print(f"\n⚠️  Просрочены напоминания для {len(overdue)} целей:")
        for g in overdue:
            days = (now - g.reminder.date).days
            print(f"   • \"{g.title}\" ({g.reminder.date.strftime('%d.%m')}) — {days} дн. просрочено")
