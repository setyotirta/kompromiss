# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: GoalLadder
class Profile:
    def __init__(self, name, goals=None):
        self.name = name
        self.goals = goals if goals is not None else []

    def add_goal(self, goal):
        self.goals.append(goal)

    def remove_goal(self, goal_title):
        return [g for g in self.goals if g.title != goal_title]

    def get_progress(self):
        total = len(self.goals)
        done = sum(1 for g in self.goals if g.is_done())
        return done / max(total, 1), done, total


class ProfileManager:
    _profiles = {}

    @classmethod
    def register(cls, profile):
        cls._profiles[profile.name] = profile

    @classmethod
    def get_profile(cls, name):
        return cls._profiles.get(name)

    @classmethod
    def list_profiles(cls):
        return list(cls._profiles.values())
