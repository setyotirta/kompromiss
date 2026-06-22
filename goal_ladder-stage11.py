# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: GoalLadder
import json, os

DATA_FILE = "goals_data.json"

def save_goals(goals):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(goals, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка сохранения] {e}")

def load_goals():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "goals" in data:
                return data["goals"]
    except (json.JSONDecodeError, IOError):
        pass
    return []

def add_goal(goal_data):
    goals = load_goals()
    goal_id = len(goals) + 1 if goals else 0
    new_goal = {**goal_data, "id": goal_id}
    goals.append(new_goal)
    save_goals(goals)
    return new_goal

def update_goal(goal_id, updates):
    goals = load_goals()
    for i, g in enumerate(goals):
        if g["id"] == goal_id:
            goals[i].update(updates)
            save_goals(goals)
            return goals[i]
    raise ValueError(f"Цель с ID {goal_id} не найдена")

def delete_goal(goal_id):
    goals = load_goals()
    for i, g in enumerate(goals):
        if g["id"] == goal_id:
            del goals[i]
            save_goals(goals)
            return True
    return False
