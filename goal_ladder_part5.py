# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GoalLadder
def delete_goal(goal_id: int) -> bool:
    """Удаление цели по ID с безопасной обработкой отсутствующей записи."""
    try:
        goals = load_goals()
        if goal_id in goals:
            del goals[goal_id]
            save_goals(goals)
            return True
        return False
    except FileNotFoundError:
        return False

def delete_step(goal_id: int, step_index: int) -> bool:
    """Удаление шага цели по ID и индексу с безопасной обработкой."""
    try:
        goals = load_goals()
        if goal_id not in goals:
            return False
        steps = goals[goal_id].get("steps", [])
        if step_index < 0 or step_index >= len(steps):
            return False
        del steps[step_index]
        # Сохраняем обновленный список шагов, если он не пустой
        if not steps:
            del goals[goal_id]["steps"]
        else:
            goals[goal_id]["steps"] = steps
        save_goals(goals)
        return True
    except (FileNotFoundError, KeyError):
        return False

def delete_achievement(goal_id: int, achievement_index: int) -> bool:
    """Удаление достижения цели по ID и индексу с безопасной обработкой."""
    try:
        goals = load_goals()
        if goal_id not in goals or "achievements" not in goals[goal_id]:
            return False
        achievements = goals[goal_id]["achievements"]
        if achievement_index < 0 or achievement_index >= len(achievements):
            return False
        del achievements[achievement_index]
        # Сохраняем обновленный список достижений, если он не пустой
        if not achievements:
            del goals[goal_id]["achievements"]
        else:
            goals[goal_id]["achievements"] = achievements
        save_goals(goals)
        return True
    except (FileNotFoundError, KeyError):
        return False
