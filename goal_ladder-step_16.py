# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GoalLadder
def calculate_monthly_stats(goals, current_date):
    from datetime import date, timedelta
    if not goals: return {}
    stats = {}
    for goal in goals:
        month_key = f"{goal['deadline'].year}-{goal['deadline'].month}"
        if month_key not in stats: stats[month_key] = {'completed': 0, 'total_steps': 0}
        steps_done = sum(1 for s in goal.get('steps', []) if s.get('done'))
        total_steps = len(goal.get('steps', []))
        stats[month_key]['completed'] += (1 if steps_done == total_steps else 0)
        stats[month_key]['total_steps'] += total_steps
    return stats
