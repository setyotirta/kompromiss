# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GoalLadder
def sort_goals(criteria='date'):
    if criteria == 'name':
        return sorted(goals, key=lambda x: (x['priority'] or 0), reverse=True)
    elif criteria == 'deadline':
        return sorted(goals, key=lambda x: x.get('due_date', ''), reverse=False)
    else:
        return goals
