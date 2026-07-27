# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: GoalLadder
class GoalTemplate:
    def __init__(self, name, description="", goal_type="Task", default_steps=3, deadline_days=None):
        self.name = name
        self.description = description
        self.goal_type = goal_type
        self.default_steps = default_steps
        self.deadline_days = deadline_days

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", "Unnamed"),
            description=data.get("description", ""),
            goal_type=data.get("goal_type", "Task"),
            default_steps=data.get("default_steps", 3),
            deadline_days=data.get("deadline_days"),
        )

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "goal_type": self.goal_type,
            "default_steps": self.default_steps,
            "deadline_days": self.deadline_days,
        }


TEMPLATES = []


def add_template(name, description="", goal_type="Task", default_steps=3, deadline_days=None):
    global TEMPLATES
    tpl = GoalTemplate(name, description, goal_type, default_steps, deadline_days)
    TEMPLATES.append(tpl)
    return tpl


add_template("Дневник привычек", "Трекер ежедневной привычки", "Habit", 30, None)
add_template("Проект с дедлайном", "Крупный проект с этапами и сроками", "Project", 5, 90)
