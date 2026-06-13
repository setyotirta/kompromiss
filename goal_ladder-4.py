# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: GoalLadder
def edit_goal(goal_id: int, updates: dict) -> Goal | None:
    for i, goal in enumerate(goals):
        if goal.id == goal_id:
            if 'title' in updates and updates['title'] is not None:
                goal.title = updates['title']
            if 'description' in updates and updates['description'] is not None:
                goal.description = updates['description']
            if 'deadline' in updates and updates['deadline'] is not None:
                goal.deadline = updates['deadline']
            if 'steps' in updates and updates['steps'] is not None:
                goal.steps.clear()
                for step_data in updates['steps']:
                    goal.steps.append(GoalStep(step_data.get('title'), step_data.get('completed', False)))
            return goal
    print(f"Goal with id {goal_id} not found.")
    return None
