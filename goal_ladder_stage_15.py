# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GoalLadder
def calculate_weekly_stats(goals: list, current_date: datetime.date) -> dict:
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'completed': 0})
    for goal in goals:
        if isinstance(goal['deadline'], str):
            deadline = datetime.strptime(goal['deadline'], '%Y-%m-%d').date()
        else:
            deadline = goal['deadline']
        week_start = (current_date - timedelta(days=current_date.weekday())).isoformat()
        week_end = (week_start + timedelta(weeks=1)).replace(day=1)
        if week_start <= deadline < week_end or week_start <= current_date < week_end:
            stats[deadline]['total'] += 1
            if goal['status'] == 'completed':
                stats[deadline]['completed'] += 1
    return dict(stats)
