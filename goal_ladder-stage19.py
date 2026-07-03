# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GoalLadder
def archive_completed_goals(goals, retention_days=365):
    from datetime import datetime, timedelta
    today = datetime.now()
    cutoff_date = today - timedelta(days=retention_days)
    archived = []
    active = []
    for goal in goals:
        if goal['status'] == 'completed':
            completed_on = datetime.strptime(goal['completed_on'], '%Y-%m-%d')
            if completed_on < cutoff_date:
                archived.append(goal.copy())
            else:
                active.append(goal)
        elif goal['deadline']:
            deadline = datetime.strptime(goal['deadline'], '%Y-%m-%d')
            if deadline > today or goal['status'] == 'in_progress':
                active.append(goal)
            else:
                archived.append(goal.copy())
        else:
            active.append(goal)
    return {'archived': archived, 'active': active}
