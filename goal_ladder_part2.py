# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GoalLadder
class Goal:
    def __init__(self, title, deadline=None):
        self.title = title
        self.deadline = deadline
        self.steps = []
        self.completed_steps = set()

    def add_step(self, step_text):
        if not step_text.strip():
            raise ValueError("Шаг не может быть пустым.")
        self.steps.append(step_text)

    def mark_complete(self, step_text):
        if step_text in self.completed_steps:
            return False
        self.completed_steps.add(step_text)
        return True

class GoalLadderApp:
    def __init__(self):
        self.goals = []

    def add_goal(self, title, deadline=None):
        if not title.strip():
            raise ValueError("Название цели не может быть пустым.")
        goal = Goal(title, deadline)
        self.goals.append(goal)
        return goal

    def validate_input(self, text):
        if not isinstance(text, str):
            return False, "Ввод должен быть строкой."
        if len(text.strip()) < 1:
            return False, "Ввод не может быть пустым."
        return True, "Валидация пройдена."

    def get_progress(self):
        total_steps = sum(len(g.steps) for g in self.goals)
        completed_steps = sum(len(g.completed_steps) for g in self.goals)
        return completed_steps / total_steps if total_steps > 0 else 0.0
