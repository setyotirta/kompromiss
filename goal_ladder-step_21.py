# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GoalLadder
class Reminder:
    def __init__(self, goal_id, message, scheduled_date):
        self.goal_id = goal_id
        self.message = message
        self.scheduled_date = scheduled_date
        self.is_sent = False

    def check(self, today):
        if not self.is_sent and self.scheduled_date <= today:
            print(f"🔔 Напоминание для цели #{self.goal_id}: {self.message}")
            self.is_sent = True
