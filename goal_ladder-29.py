# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: GoalLadder
import json

def load_settings():
    """Загрузка конфигурации из JSON с дефолтами."""
    defaults = {
        "max_goals": 10,
        "default_deadline_days": 30,
        "progress_colors": ["red", "orange", "yellow", "green"],
        "archive_after_days": 90,
        "language": "ru"
    }
    try:
        with open("settings.json", "r") as f:
            user = json.load(f)
        return {**defaults, **user}
    except FileNotFoundError:
        return defaults

def save_settings(settings):
    """Сохранение конфигурации в JSON."""
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=2)
