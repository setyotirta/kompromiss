# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GoalLadder
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Goal:
    def __init__(self, title: str, deadline: str):
        self.title = title
        self.deadline_str = deadline
        self.steps: List[Dict[str, Any]] = []
        self.completed_steps: List[int] = []
        
    def add_step(self, description: str, is_deadline_dependent: bool = False):
        step_id = len(self.steps) + 1
        self.steps.append({
            "id": step_id,
            "description": description,
            "is_deadline_dependent": is_deadline_dependent
        })
        
    def mark_step_complete(self, step_id: int):
        if step_id in self.steps and step_id not in self.completed_steps:
            self.completed_steps.append(step_id)
            
    def get_progress(self) -> float:
        total = len(self.steps)
        return (len(self.completed_steps) / total * 100) if total > 0 else 0.0
        
    def is_overdue(self) -> bool:
        try:
            deadline = datetime.strptime(self.deadline_str, "%Y-%m-%d")
            return deadline < datetime.now()
        except ValueError:
            return False

class GoalLadderApp:
    def __init__(self):
        self.goals: List[Goal] = []
        
    def add_goal(self, title: str, deadline: str) -> Goal:
        goal = Goal(title, deadline)
        self.goals.append(goal)
        return goal
        
    def get_summary(self) -> Dict[str, Any]:
        total_goals = len(self.goals)
        completed_goals = sum(1 for g in self.goals if g.get_progress() == 100.0)
        overdue_count = sum(1 for g in self.goals if g.is_overdue())
        
        return {
            "total_goals": total_goals,
            "completed_goals": completed_goals,
            "overdue_goals": overdue_count,
            "goals": [
                {
                    "title": g.title,
                    "progress": f"{g.get_progress():.1f}%",
                    "steps_count": len(g.steps),
                    "steps_completed": len(g.completed_steps),
                    "is_overdue": g.is_overdue()
                } for g in self.goals
            ]
        }

# --- Демонстрационные данные и точка входа ---

if __name__ == "__main__":
    app = GoalLadderApp()
    
    # Цель 1: Изучить Python (Дедлайн: сегодня)
    goal_1 = app.add_goal("Изучить основы Python", "2023-12-31")
    goal_1.add_step("Установить IDE и редактор кода")
    goal_1.add_step("Прочитать вводный курс по синтаксису")
    goal_1.add_step("Написать первую программу 'Hello World'")
    goal_1.mark_step_complete(1)
    
    # Цель 2: Запустить локальный бот (Дедлайн: через месяц)
    goal_2 = app.add_goal("Запустить Telegram-бота", "2024-01-31")
    goal_2.add_step("Создать структуру проекта")
    goal_2.add_step("Подключить библиотеку aiogram")
    goal_2.add_step("Реализовать обработку команд /start и /help")
    
    # Цель 3: Настроить окружение (Дедлайн: вчера - просрочено)
    goal_3 = app.add_goal("Настроить виртуальное окружение", "2023-12-30")
    goal_3.add_step("Создать venv")
    goal_3.add_step("Установить зависимости из requirements.txt")
    
    # Вывод отчета
    summary = app.get_summary()
    print(f"Всего целей: {summary['total_goals']}")
    print(f"Завершено: {summary['completed_goals']}")
    print(f"Просрочено: {summary['overdue_goals']}")
    print("\nДетали:")
    for g in summary['goals']:
        status = "⚠️ Просрочено" if g['is_overdue'] else "✅ В срок"
        print(f"- {g['title']}: {g['progress']} ({g['steps_completed']}/{g['steps_count']} шагов) [{status}]")
