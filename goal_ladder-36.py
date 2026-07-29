# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GoalLadder
def integrity_check_and_repair():
    """Проверяет целостность данных и пытается исправить простые проблемы."""
    issues = []
    
    # Проверяем, что цели имеют ID
    for i, goal in enumerate(goals):
        if not isinstance(goal['id'], int) or goal['id'] <= 0:
            goal['id'] = i + 1
            issues.append(f"Исправлен ID цели {goal['title']}")
    
    # Проверяем шаги на наличие обязательных полей
    for i, step in enumerate(steps):
        if 'goal_id' not in step or not isinstance(step['goal_id'], int):
            steps[i]['goal_id'] = 1
            issues.append(f"Исправлен goal_id шага {step.get('title', f'step_{i}')}")
    
    # Проверяем, что цели имеют статус (если не задан)
    for i, goal in enumerate(goals):
        if 'status' not in goal or goal['status'] == '':
            goal['status'] = 'active'
            issues.append(f"Исправлен статус цели {goal.get('title', f'goal_{i}')}")
    
    # Проверяем, что у шагов есть порядок (если не задан)
    for i, step in enumerate(steps):
        if 'order' not in step or step['order'] == 0:
            step['order'] = len(goals) * steps + i + 1
            issues.append(f"Исправлен order шага {step.get('title', f'step_{i}')}")
    
    print("Проверка целостности завершена.")
    if issues:
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("Все данные корректны!")
