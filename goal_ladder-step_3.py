# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GoalLadder
class GoalLadder:
    def __init__(self):
        self.goals = []
        self.achievements = []

    def add_goal(self, title, steps=None, deadline=None):
        goal = {
            "id": len(self.goals) + 1,
            "title": title,
            "steps": steps or [],
            "deadline": deadline,
            "status": "active",
            "created_at": self._now()
        }
        self.goals.append(goal)
        return goal

    def add_step(self, goal_id, step_text):
        for goal in self.goals:
            if goal["id"] == goal_id and goal["status"] != "completed":
                goal["steps"].append(step_text)
                return True
        return False

    def mark_step_done(self, goal_id, step_index):
        for goal in self.goals:
            if goal["id"] == goal_id and step_index < len(goal["steps"]):
                goal["steps"][step_index] = f"[x] {goal['steps'][step_index]}"
                return True
        return False

    def complete_goal(self, goal_id):
        for goal in self.goals:
            if goal["id"] == goal_id and goal["status"] != "completed":
                goal["status"] = "completed"
                self.achievements.append({
                    "goal_id": goal_id,
                    "title": goal["title"],
                    "completed_at": self._now()
                })
                return True
        return False

    def _now(self):
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
