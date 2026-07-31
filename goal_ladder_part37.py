# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GoalLadder
import unittest


class TestGoalLadder(unittest.TestCase):

    def test_add_goal(self):
        app = GoalLadder()
        app.add_goal("Бег", "10 км/неделю")
        self.assertEqual(len(app.goals), 1)
        self.assertIn("Бег", [g.name for g in app.goals])

    def test_add_step(self):
        app = GoalLadder()
        goal = app.add_goal("Бег", "10 км/неделю")
        app.add_step(goal, "План тренировок")
        self.assertEqual(len(goal.steps), 1)

    def test_mark_complete(self):
        app = GoalLadder()
        goal = app.add_goal("Чтение", "5 книг")
        step = app.add_step(goal, "Книга 1: Python для начинающих")
        app.mark_complete(step)
        self.assertTrue(step.completed)

    def test_progress_percentage(self):
        app = GoalLadder()
        goal = app.add_goal("Бег", "10 км/неделю")
        app.add_step(goal, "Понедельник: 2 км")
        app.add_step(goal, "Среда: 3 км")
        app.mark_complete(app.steps[0])
        pct = goal.progress_percentage()
        self.assertAlmostEqual(pct, 1 / (len(goal.steps) - 1), places=5)

    def test_add_deadline(self):
        app = GoalLadder()
        goal = app.add_goal("Диплом", "Защита проекта")
        app.add_step(goal, "Написать введение")
        deadline = Deadline(2026, 12, 31)
        app.add_deadline(goal, deadline)
        self.assertEqual(len(goal.deadlines), 1)

    def test_due_date_format(self):
        d = Deadline(2026, 5, 15)
        self.assertIn("05.05", repr(d))


if __name__ == "__main__":
    unittest.main()
