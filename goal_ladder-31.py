# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: GoalLadder
class UserSwitcher:
    """Переключение активного профиля пользователя."""

    def __init__(self, profiles):
        self.profiles = profiles
        self.active_id = None

    @property
    def active_profile(self):
        if not self.profiles or self.active_id is None:
            return None
        return self.profiles.get(self.active_id)

    def switch_to(self, profile_id):
        """Перейти к профилю по ID."""
        if not self.profiles:
            raise ValueError("Нет доступных профилей")
        if profile_id not in self.profiles:
            raise KeyError(f"Профиль '{profile_id}' не найден. Доступные: {list(self.profiles.keys())}")
        self.active_id = profile_id
