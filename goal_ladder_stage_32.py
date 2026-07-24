# === Stage 32: Добавь журнал действий пользователя ===
# Project: GoalLadder
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, detail=""):
        entry = {
            "user": user,
            "timestamp": datetime.now(),
            "type": action_type,
            "detail": detail,
        }
        self.entries.append(entry)

    def get_recent(self, count=10):
        return self.entries[-count:]

    def get_by_user(self, user, days=30):
        cutoff = datetime.now() - timedelta(days=days)
        return [e for e in self.entries if e["user"] == user and e["timestamp"] > cutoff]

    def get_summary(self):
        stats = {}
        today = date.today().isoformat()
        for entry in self.entries:
            key = f"{entry['type']}:{entry['detail']}"
            stats[key] = stats.get(key, 0) + 1
        return stats

    def display(self):
        print("\n📋 Лог действий:")
        recent = self.get_recent(5)
        if not recent:
            print("Пока пусто.")
        else:
            for e in reversed(recent):
                dt = e["timestamp"].strftime("%d.%m %H:%M")
                print(f"  [{dt}] {e['user']}: {e['type']} — {e['detail']}")

    def display_summary(self):
        stats = self.get_summary()
        if not stats:
            print("📊 Статистика пуста.")
        else:
            lines = ["📊 Итого действий (все время):"]
            for k, v in sorted(stats.items(), key=lambda x: -x[1]):
                lines.append(f"  {k}: {v} раз")
            print("\n".join(lines))

    def display_user_history(self, user="Алексей"):
        history = self.get_by_user(user)
        if not history:
            print(f"📜 История {user}: пусто.")
        else:
            lines = [f"📜 Действия {user} за последние 30 дней:", ""]
            for e in reversed(history):
                dt = e["timestamp"].strftime("%d.%m %H:%M")
                lines.append(f"  [{dt}] {e['type']} — {e['detail']}")
            print("\n".join(lines))

    def clear(self):
        self.entries.clear()
