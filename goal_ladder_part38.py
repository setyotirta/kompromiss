# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: GoalLadder
import unittest

class TestGoalLadderEdgeCases(unittest.TestCase):

    def setUp(self):
        from src.goal import Goal, Step
        self.goal = Goal("Test Goal", "2024-12-31")
        for i in range(5):
            step = Step(f"Step {i+1}", done=i < 3)
            self.goal.add_step(step)

    def test_goal_complete(self):
        self.assertTrue(self.goal.is_complete())

    def test_goal_incomplete(self):
        goal2 = Goal("Incomplete", "2024-12-31")
        for i in range(5):
            step = Step(f"Step {i+1}", done=False)
            goal2.add_step(step)
        self.assertFalse(goal2.is_complete())

    def test_goal_empty(self):
        g = Goal("Empty", "2024-12-31")
        self.assertEqual(g.progress, 0.0)
        self.assertEqual(len(g.steps), 0)

    def test_add_step_after_completion_raises(self):
        goal = Goal("Final", "2024-12-31")
        step = Step("Last", done=True)
        goal.add_step(step)
        with self.assertRaises(ValueError):
            goal.add_step(Step("Extra", done=False))

    def test_remove_nonexistent_step_raises(self):
        goal = Goal("Test", "2024-12-31")
        step = Step("S", done=True)
        goal.add_step(step)
        with self.assertRaises(ValueError):
            goal.remove_step(Step("Nope", done=False))

    def test_remove_complete_goal_raises(self):
        goal = Goal("Done", "2024-12-31")
        step = Step("S", done=True)
        goal.add_step(step)
        with self.assertRaises(ValueError):
            goal.remove()

    def test_progress_calculation(self):
        g = Goal("Halfway", "2025-06-01")
        s = [Step(f"S{i}", done=i == 1) for i in range(3)]
        for step in s:
            g.add_step(step)
        self.assertEqual(g.progress, 1.0 / 3.0)

    def test_bad_deadline_format(self):
        with self.assertRaises(ValueError):
            Goal("Bad Date", "not-a-date")

    def test_goal_with_no_steps_progress_zero(self):
        g = Goal("Just Started", "2025-12-31")
        self.assertEqual(g.progress, 0.0)

if __name__ == "__main__":
    unittest.main()
