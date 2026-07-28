# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: GoalLadder
def get_next_action(goal, actions_history):
    """Рекомендует следующее действие на основе прогресса и истории."""
    if goal["completed"]:
        return None
    
    steps = goal.get("steps", [])
    
    # Если шаги определены — проверяем текущий статус
    if steps:
        current_step = next((s for s in steps if not s.get("done")), None)
        
        if current_step and "action" in current_step:
            return {
                "type": "step",
                "goal_id": goal["id"],
                "action": current_step["action"],
                "description": f"Выполните шаг: {current_step['action']}"
            }
        
        # Если шаги без действий, но есть прогресс — рекомендуйте продолжение
        if any(s.get("done") for s in steps):
            return {
                "type": "continue",
                "goal_id": goal["id"],
                "description": f"Продолжайте работу над целью: {goal['title']}"
            }
    
    # Если есть дедлайн и он близок — предупреждение
    deadline = goal.get("deadline")
    if deadline and (deadline - datetime.now()).days <= 3:
        return {
            "type": "warning",
            "goal_id": goal["id"],
            "description": f"Дедлайн скоро! Обновите статус цели: {goal['title']}"
        }
    
    # Если есть прогресс и история — рекомендуйте следующий шаг
    if goal.get("progress") and actions_history:
        last_action = actions_history[-1]
        if last_action.get("type") == "step" and last_action.get("action"):
            return {
                "type": "continue",
                "goal_id": goal["id"],
                "description": f"Следующий шаг для: {goal['title']}"
            }
    
    # Если совсем пусто — начните планировать
    if not goal.get("steps") and not goal.get("progress"):
        return {
            "type": "plan",
            "goal_id": goal["id"],
            "description": f"Создайте план действий для: {goal['title']}"
        }
    
    # По умолчанию — обобщённая рекомендация
    return {
        "type": "general",
        "goal_id": goal["id"],
        "description": f"Продолжайте работу над целью: {goal['title']}"
    }
